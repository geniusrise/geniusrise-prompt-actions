import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# List Voice Regions
def list_voice_regions(token: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all available voice regions in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the voice regions or an error message.
    """
    url = "https://discord.com/api/v9/voice/regions"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Current Voice State
def get_current_voice_state(token: str, guild_id: str, user_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the current voice state of a user in a specific guild.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild.
    - user_id (str): The ID of the user whose voice state is to be retrieved.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the voice state or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/voice-states/{user_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Voice State
def update_voice_state(
    token: str, guild_id: str, channel_id: str, user_id: str, self_mute: bool, self_deaf: bool
) -> Union[Dict[str, Any], str]:
    """
    Updates the voice state of a user in a specific guild.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild.
    - channel_id (str): The ID of the voice channel.
    - user_id (str): The ID of the user whose voice state is to be updated.
    - self_mute (bool): Whether the user is muted.
    - self_deaf (bool): Whether the user is deafened.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the updated voice state or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/voice-states/{user_id}"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"channel_id": channel_id, "self_mute": self_mute, "self_deaf": self_deaf}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
