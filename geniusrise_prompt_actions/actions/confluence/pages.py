import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Create Page
def create_page(base_url: str, auth: tuple, space_key: str, title: str, content: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new page in a Confluence space.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - space_key (str): The key of the space where the page will be created.
    - title (str): The title of the new page.
    - content (str): The content of the new page in Confluence storage format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content"
    headers = {"Content-Type": "application/json"}
    payload = {
        "type": "page",
        "title": title,
        "space": {"key": space_key},
        "body": {"storage": {"value": content, "representation": "storage"}},
    }

    try:
        response = requests.post(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Page
def read_page(base_url: str, auth: tuple, page_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a Confluence page by its ID.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Page
def update_page(
    base_url: str, auth: tuple, page_id: str, version: int, title: str, content: str
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page to update.
    - version (int): The current version number of the page.
    - title (str): The new title for the page.
    - content (str): The new content for the page in Confluence storage format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "version": {"number": version + 1},
        "title": title,
        "type": "page",
        "body": {"storage": {"value": content, "representation": "storage"}},
    }

    try:
        response = requests.put(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Page
def delete_page(base_url: str, auth: tuple, page_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a Confluence page by its ID.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}"

    try:
        response = requests.delete(url, auth=auth)
        response.raise_for_status()
        return {"status": "Page deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Pages by Space
def list_pages_by_space(base_url: str, auth: tuple, space_key: str, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Lists all pages in a Confluence space.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - space_key (str): The key of the space to list pages from.
    - limit (int, optional): The maximum number of pages to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content"
    params = {"spaceKey": space_key, "limit": limit, "type": "page"}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
