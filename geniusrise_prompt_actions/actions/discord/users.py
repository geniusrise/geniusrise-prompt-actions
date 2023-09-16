import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Get User Details
def get_user_details(token: str, user_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a specific user in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - user_id (str): The ID of the user whose details are to be retrieved.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/users/{user_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update User Details
# Note: Bots cannot update user details, only applicable for user accounts
# This function is left for reference and should be used carefully
def update_user_details(token: str, user_id: str, username: str, avatar: str) -> Union[Dict[str, Any], str]:
    """
    Updates the details of a specific user in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - user_id (str): The ID of the user whose details are to be updated.
    - username (str): The new username for the user.
    - avatar (str): The new avatar URL for the user.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/users/{user_id}"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"username": username, "avatar": avatar}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Members in a Guild
def list_all_members(token: str, guild_id: str, limit: int = 1000) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all members in a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild whose members are to be listed.
    - limit (int): The number of members to retrieve (default is 1000).

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the members or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members?limit={limit}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
