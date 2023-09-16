import requests  # type: ignore
import logging
from typing import Union, Dict, Any, List


# List Channels
def list_channels(token: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all channels in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the channels or an error message.
    """
    url = "https://slack.com/api/conversations.list"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("channels", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Channel
def create_channel(token: str, name: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - name (str): The name of the new channel.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.create"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": name}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Join Channel
def join_channel(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Joins a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to join.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.join"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Leave Channel
def leave_channel(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Leaves a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to leave.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.leave"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Archive Channel
def archive_channel(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Archives a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to archive.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.archive"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unarchive Channel
def unarchive_channel(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Unarchives a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to unarchive.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.unarchive"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Rename Channel
def rename_channel(token: str, channel_id: str, new_name: str) -> Union[Dict[str, Any], str]:
    """
    Renames a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to rename.
    - new_name (str): The new name for the channel.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.rename"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "name": new_name}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Channel Info
def get_channel_info(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves information about a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to get information about.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.info"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"channel": channel_id}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Set Channel Topic
def set_channel_topic(token: str, channel_id: str, topic: str) -> Union[Dict[str, Any], str]:
    """
    Sets the topic of a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to set the topic for.
    - topic (str): The new topic for the channel.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.setTopic"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "topic": topic}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Set Channel Purpose
def set_channel_purpose(token: str, channel_id: str, purpose: str) -> Union[Dict[str, Any], str]:
    """
    Sets the purpose of a channel in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to set the purpose for.
    - purpose (str): The new purpose for the channel.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.setPurpose"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "purpose": purpose}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
