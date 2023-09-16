import requests  # type: ignore
from typing import Union, Dict, Any
import logging


def add_page_permissions(
    base_url: str, auth: tuple, page_id: str, permissions: Dict[str, Any]
) -> Union[Dict[str, Any], str]:
    """
    Adds permissions to a specific page in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page where permissions will be added.
    - permissions (Dict[str, Any]): A dictionary containing the permissions to be added.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/restriction"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=permissions, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove Page Permissions
def remove_page_permissions(
    base_url: str, auth: tuple, page_id: str, permissions: Dict[str, Any]
) -> Union[Dict[str, Any], str]:
    """
    Removes permissions from a specific page in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page where permissions will be removed.
    - permissions (Dict[str, Any]): A dictionary containing the permissions to be removed.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/restriction"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, json=permissions, auth=auth)
        response.raise_for_status()
        return {"status": "Permissions removed successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Page Permissions
def list_page_permissions(base_url: str, auth: tuple, page_id: str) -> Union[Dict[str, Any], str]:
    """
    Lists all permissions on a specific page in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page whose permissions will be listed.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/restriction"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
