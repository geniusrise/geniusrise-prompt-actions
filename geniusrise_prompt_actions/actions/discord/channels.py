import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Create Channel
def create_channel(token: str, guild_id: str, channel_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
    """
    Creates a new channel in a Discord guild.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild where the channel will be created.
    - channel_data (Dict[str, Any]): A dictionary containing the channel data.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=channel_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Channel Details
def get_channel_details(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves details of a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Channel
def update_channel(token: str, channel_id: str, update_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
    """
    Updates details of a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel.
    - update_data (Dict[str, Any]): A dictionary containing the data to update.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}

    try:
        response = requests.patch(url, headers=headers, json=update_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Channel
def delete_channel(token: str, channel_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"status": "Channel deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Channels in a Guild
def list_all_channels(token: str, guild_id: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all channels in a specific Discord guild.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the channels or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
