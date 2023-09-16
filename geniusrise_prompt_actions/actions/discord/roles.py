import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Create Role
def create_role(token: str, guild_id: str, name: str, permissions: int, color: int) -> Union[Dict[str, Any], str]:
    """
    Creates a new role in a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild where the role will be created.
    - name (str): The name of the new role.
    - permissions (int): The permission bitfield for the role.
    - color (int): The color of the role in integer format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"name": name, "permissions": permissions, "color": color}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Role Details
def get_role_details(token: str, guild_id: str, role_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a specific role in a guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild where the role exists.
    - role_id (str): The ID of the role whose details are to be retrieved.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Role
def update_role(
    token: str, guild_id: str, role_id: str, name: str, permissions: int, color: int
) -> Union[Dict[str, Any], str]:
    """
    Updates the details of a specific role in a guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild where the role exists.
    - role_id (str): The ID of the role to be updated.
    - name (str): The new name for the role.
    - permissions (int): The new permission bitfield for the role.
    - color (int): The new color for the role in integer format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"name": name, "permissions": permissions, "color": color}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Role
def delete_role(token: str, guild_id: str, role_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a specific role in a guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild where the role exists.
    - role_id (str): The ID of the role to be deleted.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles/{role_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Roles in a Guild
def list_all_roles(token: str, guild_id: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all roles in a specific guild (server) in Discord.

    Parameters:
    - token (str): The authentication token for Discord API.
    - guild_id (str): The ID of the guild whose roles are to be listed.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the roles or an error message.
    """
    url = f"https://discord.com/api/v9/guilds/{guild_id}/roles"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
