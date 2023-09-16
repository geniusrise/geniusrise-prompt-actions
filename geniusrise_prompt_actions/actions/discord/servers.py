import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Create Guild
def create_guild(token: str, guild_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
    """
    Creates a new guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_data (Dict[str, Any]): A dictionary containing the guild data.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = "https://discord.com/api/v9/guilds"
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=guild_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Guild Details
def get_guild_details(token: str, guild_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves details of a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Guild
def update_guild(token: str, guild_id: str, update_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
    """
    Updates details of a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild.
    - update_data (Dict[str, Any]): A dictionary containing the data to update.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}"
    headers = {"Authorization": f"Bot {token}", "Content-Type": "application/json"}

    try:
        response = requests.patch(url, headers=headers, json=update_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Guild
def delete_guild(token: str, guild_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return {"status": "Guild deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Guilds
def list_all_guilds(token: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all guilds (servers) the bot is a member of.

    Parameters:
    - token (str): The authentication token for Discord API.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the guilds or an error message.
    """
    url = "https://discord.com/api/v9/users/@me/guilds"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
