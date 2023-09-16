import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Create Webhook
def create_webhook(token: str, channel_id: str, name: str, avatar: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new webhook for a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel where the webhook will be created.
    - name (str): The name of the webhook.
    - avatar (str): The avatar URL for the webhook. Optional.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"name": name, "avatar": avatar}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Webhook Details
def get_webhook_details(token: str, webhook_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a specific webhook in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - webhook_id (str): The ID of the webhook whose details are to be retrieved.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/webhooks/{webhook_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Webhook
def update_webhook(token: str, webhook_id: str, name: str, avatar: str) -> Union[Dict[str, Any], str]:
    """
    Updates the details of a specific webhook in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - webhook_id (str): The ID of the webhook to be updated.
    - name (str): The new name for the webhook.
    - avatar (str): The new avatar URL for the webhook. Optional.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/webhooks/{webhook_id}"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"name": name, "avatar": avatar}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Webhook
def delete_webhook(token: str, webhook_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a specific webhook in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - webhook_id (str): The ID of the webhook to be deleted.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/webhooks/{webhook_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Webhooks in a Guild
def list_all_webhooks(token: str, guild_id: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all webhooks in a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild whose webhooks are to be listed.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the webhooks or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/webhooks"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
