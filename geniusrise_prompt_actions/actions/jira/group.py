import logging
from typing import Dict, List, Any, Union

import requests  # type: ignore


# Create Group
def create_group(server_url: str, auth: Dict[str, str], group_name: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new group in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - group_name (str): The name of the new group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/group"
    headers = {"Content-Type": "application/json"}
    payload = {"name": group_name}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Group
def read_group(server_url: str, auth: Dict[str, str], group_name: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves a group from Jira by its name.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - group_name (str): The name of the group to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/group"
    headers = {"Content-Type": "application/json"}
    params = {"groupname": group_name}

    try:
        response = requests.get(url, headers=headers, params=params, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Group
def update_group(server_url: str, auth: Dict[str, str], group_name: str, new_name: str) -> Union[Dict[str, Any], str]:
    """
    Updates a group's name in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - group_name (str): The current name of the group.
    - new_name (str): The new name for the group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    # Note: Jira API may not support group name updates directly. This is a placeholder.
    # You may need to delete and recreate the group or use other methods to achieve this.
    logging.warning("Jira API may not support direct group name updates. This is a placeholder function.")
    return "Group update feature may not be supported by Jira API."


# Delete Group
def delete_group(server_url: str, auth: Dict[str, str], group_name: str) -> str:
    """
    Deletes a group from Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - group_name (str): The name of the group to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/group"
    headers = {"Content-Type": "application/json"}
    params = {"groupname": group_name}

    try:
        response = requests.delete(url, headers=headers, params=params, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Group deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Groups
def list_all_groups(server_url: str, auth: Dict[str, str]) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all groups in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the groups or an error message.
    """
    url = f"{server_url}/rest/api/2/groups/picker"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json().get("groups", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
