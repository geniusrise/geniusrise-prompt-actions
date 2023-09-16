import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Create Comment
def create_comment(base_url: str, auth: tuple, page_id: str, content: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new comment on a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page where the comment will be created.
    - content (str): The content of the comment in Confluence storage format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/child/comment"
    headers = {"Content-Type": "application/json"}
    payload = {"type": "comment", "body": {"storage": {"value": content, "representation": "storage"}}}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Comment
def read_comment(base_url: str, auth: tuple, comment_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a Confluence comment by its ID.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - comment_id (str): The ID of the comment to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{comment_id}"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Comment
def update_comment(
    base_url: str, auth: tuple, comment_id: str, version: int, content: str
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing Confluence comment.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - comment_id (str): The ID of the comment to update.
    - version (int): The current version number of the comment.
    - content (str): The new content for the comment in Confluence storage format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{comment_id}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "version": {"number": version + 1},
        "type": "comment",
        "body": {"storage": {"value": content, "representation": "storage"}},
    }

    try:
        response = requests.put(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Comment
def delete_comment(base_url: str, auth: tuple, comment_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a Confluence comment by its ID.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - comment_id (str): The ID of the comment to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{comment_id}"

    try:
        response = requests.delete(url, auth=auth)
        response.raise_for_status()
        return {"status": "Comment deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Comments on a Page
def list_comments_on_page(base_url: str, auth: tuple, page_id: str, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Lists all comments on a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page to list comments from.
    - limit (int, optional): The maximum number of comments to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/child/comment"
    params = {"limit": limit}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
