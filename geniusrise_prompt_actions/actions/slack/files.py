import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# Upload File
def upload_file(token: str, channels: str, file_path: str) -> Union[Dict[str, Any], str]:
    """
    Uploads a file to a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channels (str): Comma-separated list of channel IDs where the file will be shared.
    - file_path (str): The local path to the file to be uploaded.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/files.upload"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channels": channels}
    files = {"file": open(file_path, "rb")}

    try:
        response = requests.post(url, headers=headers, data=payload, files=files)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Share File
def share_file(token: str, file_id: str, channels: str) -> Union[Dict[str, Any], str]:
    """
    Shares an already uploaded file to additional Slack channels.

    Parameters:
    - token (str): The authentication token for Slack API.
    - file_id (str): The ID of the file to be shared.
    - channels (str): Comma-separated list of channel IDs where the file will be shared.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/files.sharedPublicURL"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"file": file_id, "channels": channels}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete File
def delete_file(token: str, file_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a file from Slack.

    Parameters:
    - token (str): The authentication token for Slack API.
    - file_id (str): The ID of the file to be deleted.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/files.delete"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"file": file_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Files
def list_files(token: str) -> Union[Dict[str, Any], str]:
    """
    Lists all files that are currently available in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/files.list"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
