import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# List Conversations
def list_conversations(token: str) -> Union[Dict[str, Any], str]:
    """
    Lists all conversations in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.list"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Open Conversation
def open_conversation(token: str, user_ids: str) -> Union[Dict[str, Any], str]:
    """
    Opens a conversation with one or more users in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - user_ids (str): Comma-separated list of user IDs to open a conversation with.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.open"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"users": user_ids}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Close Conversation
def close_conversation(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Closes a conversation in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to close.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.close"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Invite Users to Conversation
def invite_users_to_conversation(token: str, channel_id: str, user_ids: str) -> Union[Dict[str, Any], str]:
    """
    Invites one or more users to a conversation in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to invite users to.
    - user_ids (str): Comma-separated list of user IDs to invite.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.invite"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "users": user_ids}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Kick User from Conversation
def kick_user_from_conversation(token: str, channel_id: str, user_id: str) -> Union[Dict[str, Any], str]:
    """
    Removes a user from a conversation in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to remove the user from.
    - user_id (str): The ID of the user to remove.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.kick"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "user": user_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
