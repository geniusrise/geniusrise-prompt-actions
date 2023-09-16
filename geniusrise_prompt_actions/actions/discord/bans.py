import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Ban User
def ban_user(
    token: str, guild_id: str, user_id: str, delete_message_days: int = 0, reason: str = "None"
) -> Union[Dict[str, Any], str]:
    """
    Bans a user from a specific guild in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild where the user will be banned.
    - user_id (str): The ID of the user to be banned.
    - delete_message_days (int): Number of days to delete messages for (0-7). Default is 0.
    - reason (str): The reason for the ban. Optional.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/bans/{user_id}"
    headers = {"Authorization": f"Bot {token}"}
    params = {"delete_message_days": delete_message_days, "reason": reason}

    try:
        response = requests.put(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unban User
def unban_user(token: str, guild_id: str, user_id: str) -> Union[Dict[str, Any], str]:
    """
    Unbans a user from a specific guild in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild where the user will be unbanned.
    - user_id (str): The ID of the user to be unbanned.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/bans/{user_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Bans in a Guild
def list_all_bans(token: str, guild_id: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all bans in a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild whose bans are to be listed.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the bans or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/bans"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
