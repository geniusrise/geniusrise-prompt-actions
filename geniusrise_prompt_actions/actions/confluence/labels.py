import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Add Label to Page
def add_label_to_page(base_url: str, auth: tuple, page_id: str, label: str) -> Union[Dict[str, Any], str]:
    """
    Adds a label to a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page where the label will be added.
    - label (str): The label to add to the page.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/label"
    headers = {"Content-Type": "application/json"}
    payload = {"name": label}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove Label from Page
def remove_label_from_page(base_url: str, auth: tuple, page_id: str, label: str) -> Union[Dict[str, Any], str]:
    """
    Removes a label from a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page from which the label will be removed.
    - label (str): The label to remove from the page.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/label/{label}"

    try:
        response = requests.delete(url, auth=auth)
        response.raise_for_status()
        return {"status": "Label removed successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Labels on a Page
def list_labels_on_page(base_url: str, auth: tuple, page_id: str, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Lists all labels on a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page to list labels from.
    - limit (int, optional): The maximum number of labels to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/label"
    params = {"limit": limit}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
