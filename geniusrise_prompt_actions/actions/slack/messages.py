import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# Update Message
def update_message(token: str, channel_id: str, ts: str, text: str) -> Union[Dict[str, Any], str]:
    """
    Updates a message in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel where the message exists.
    - ts (str): The timestamp of the message to update.
    - text (str): The new text for the message.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/chat.update"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "ts": ts, "text": text}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Message
def delete_message(token: str, channel_id: str, ts: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a message in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel where the message exists.
    - ts (str): The timestamp of the message to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/chat.delete"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "ts": ts}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Messages in a Channel
def list_messages_in_channel(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Lists messages in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel to list messages from.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/conversations.history"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id}

    try:
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# React to a Message
def react_to_message(token: str, channel_id: str, ts: str, emoji: str) -> Union[Dict[str, Any], str]:
    """
    Adds a reaction to a message in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel where the message exists.
    - ts (str): The timestamp of the message to react to.
    - emoji (str): The emoji to use for the reaction.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reactions.add"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "timestamp": ts, "name": emoji}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unreact to a Message
def unreact_to_message(token: str, channel_id: str, ts: str, emoji: str) -> Union[Dict[str, Any], str]:
    """
    Removes a reaction from a message in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel_id (str): The ID of the channel where the message exists.
    - ts (str): The timestamp of the message to unreact to.
    - emoji (str): The emoji to remove from the reaction.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reactions.remove"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel_id, "timestamp": ts, "name": emoji}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
