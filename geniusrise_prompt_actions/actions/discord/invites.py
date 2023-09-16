import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Create Invite
def create_invite(token: str, channel_id: str, max_age: int = 3600, max_uses: int = 0) -> Union[Dict[str, Any], str]:
    """
    Creates a new invite for a specific channel in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - channel_id (str): The ID of the channel where the invite will be created.
    - max_age (int): Duration of invite in seconds before expiry. Default is 3600 seconds (1 hour).
    - max_uses (int): Maximum number of uses for the invite. Default is 0 (unlimited).

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/invites"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"max_age": max_age, "max_uses": max_uses}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Invite Details
def get_invite_details(token: str, invite_code: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a specific invite in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - invite_code (str): The code of the invite whose details are to be retrieved.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/invites/{invite_code}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Invite
def delete_invite(token: str, invite_code: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a specific invite in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - invite_code (str): The code of the invite to be deleted.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/invites/{invite_code}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Invites in a Guild
def list_all_invites(token: str, guild_id: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all invites in a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild whose invites are to be listed.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the invites or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/invites"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
