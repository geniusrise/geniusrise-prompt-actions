import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Create Group
def create_group(base_url: str, auth: tuple, group_name: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new group in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - group_name (str): The name of the group to be created.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/group"
    headers = {"Content-Type": "application/json"}
    payload = {"name": group_name}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Group
def delete_group(base_url: str, auth: tuple, group_name: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a group in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - group_name (str): The name of the group to be deleted.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/group"
    params = {"groupname": group_name}

    try:
        response = requests.delete(url, params=params, auth=auth)
        response.raise_for_status()
        return {"status": "Group deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add User to Group
def add_user_to_group(base_url: str, auth: tuple, group_name: str, username: str) -> Union[Dict[str, Any], str]:
    """
    Adds a user to a group in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - group_name (str): The name of the group where the user will be added.
    - username (str): The username of the user to be added to the group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/group/user"
    params = {"groupname": group_name}
    headers = {"Content-Type": "application/json"}
    payload = {"name": username}

    try:
        response = requests.post(url, params=params, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove User from Group
def remove_user_from_group(base_url: str, auth: tuple, group_name: str, username: str) -> Union[Dict[str, Any], str]:
    """
    Removes a user from a group in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - group_name (str): The name of the group from which the user will be removed.
    - username (str): The username of the user to be removed from the group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/group/user"
    params = {"groupname": group_name, "username": username}

    try:
        response = requests.delete(url, params=params, auth=auth)
        response.raise_for_status()
        return {"status": "User removed from group successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Groups
def list_all_groups(base_url: str, auth: tuple, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Lists all groups in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - limit (int, optional): The maximum number of groups to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/group"
    params = {"limit": limit}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
