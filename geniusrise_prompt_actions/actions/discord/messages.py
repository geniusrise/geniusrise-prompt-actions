import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Send Message
def send_message(token: str, channel_id: str, content: str) -> Union[Dict[str, Any], str]:
    """
    Sends a message to a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel where the message will be sent.
    - content (str): The content of the message.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}
    payload = {"content": content}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Edit Message
def edit_message(token: str, channel_id: str, message_id: str, new_content: str) -> Union[Dict[str, Any], str]:
    """
    Edits a message in a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel where the message exists.
    - message_id (str): The ID of the message to edit.
    - new_content (str): The new content for the message.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}
    payload = {"content": new_content}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Message
def delete_message(token: str, channel_id: str, message_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a message in a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel where the message exists.
    - message_id (str): The ID of the message to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"status": "Message deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Messages in a Channel
def list_messages(token: str, channel_id: str, limit: int = 50) -> Union[List[Dict[str, Any]], str]:
    """
    Lists messages in a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel.
    - limit (int): The number of messages to retrieve (default is 50).

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the messages or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Pin Message
def pin_message(token: str, channel_id: str, message_id: str) -> Union[Dict[str, Any], str]:
    """
    Pins a message in a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel where the message exists.
    - message_id (str): The ID of the message to pin.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/pins/{message_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.put(url, headers=headers)
        response.raise_for_status()
        return {"status": "Message pinned successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unpin Message
def unpin_message(token: str, channel_id: str, message_id: str) -> Union[Dict[str, Any], str]:
    """
    Unpins a message in a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel where the message exists.
    - message_id (str): The ID of the message to unpin.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/pins/{message_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"status": "Message unpinned successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
