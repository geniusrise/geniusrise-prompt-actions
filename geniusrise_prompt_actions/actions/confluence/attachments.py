import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Upload Attachment
def upload_attachment(base_url: str, auth: tuple, page_id: str, file_path: str) -> Union[Dict[str, Any], str]:
    """
    Uploads an attachment to a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page where the attachment will be uploaded.
    - file_path (str): The path to the file to be uploaded.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/child/attachment"
    headers = {"X-Atlassian-Token": "no-check"}

    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, headers=headers, files=files, auth=auth)
            response.raise_for_status()
            return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Download Attachment
def download_attachment(base_url: str, auth: tuple, attachment_id: str, save_path: str) -> Union[str, None]:
    """
    Downloads an attachment from a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - attachment_id (str): The ID of the attachment to download.
    - save_path (str): The path where the downloaded file will be saved.

    Returns:
    - Union[str, None]: An error message or None if successful.
    """
    url = f"{base_url}/rest/api/content/{attachment_id}/download"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(response.content)
        return None
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Attachment
def delete_attachment(base_url: str, auth: tuple, attachment_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes an attachment from a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - attachment_id (str): The ID of the attachment to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{attachment_id}"

    try:
        response = requests.delete(url, auth=auth)
        response.raise_for_status()
        return {"status": "Attachment deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Attachments on a Page
def list_attachments_on_page(base_url: str, auth: tuple, page_id: str, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Lists all attachments on a Confluence page.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - page_id (str): The ID of the page to list attachments from.
    - limit (int, optional): The maximum number of attachments to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/{page_id}/child/attachment"
    params = {"limit": limit}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
