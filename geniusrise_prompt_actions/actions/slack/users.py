import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# List Users
def list_users(token: str) -> Union[Dict[str, Any], str]:
    """
    Lists all users in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/users.list"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get User Info
def get_user_info(token: str, user_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves information about a user in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - user_id (str): The ID of the user to get information about.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/users.info"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"user": user_id}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Set User Status
def set_user_status(token: str, status_text: str, status_emoji: str) -> Union[Dict[str, Any], str]:
    """
    Sets the status of the authenticated user in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - status_text (str): The text that appears in the status.
    - status_emoji (str): The emoji that appears in the status.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/users.profile.set"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"profile": {"status_text": status_text, "status_emoji": status_emoji}}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Set User Presence
def set_user_presence(token: str, presence: str) -> Union[Dict[str, Any], str]:
    """
    Sets the presence of the authenticated user in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - presence (str): The presence status to set ('auto' or 'away').

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/users.setPresence"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"presence": presence}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
