import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# Create Group
def create_group(server_url: str, auth_token: str, name: str, path: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new group in GitLab.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - name (str): The name of the new group.
    - path (str): The path for the new group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/groups"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": name, "path": path}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Group
def read_group(server_url: str, auth_token: str, group_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves details of a GitLab group by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - group_id (int): The ID of the group to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/groups/{group_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Group
def update_group(server_url: str, auth_token: str, group_id: int, name: str, path: str) -> Union[Dict[str, Any], str]:
    """
    Updates details of a GitLab group by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - group_id (int): The ID of the group to update.
    - name (str): The new name of the group.
    - path (str): The new path for the group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/groups/{group_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": name, "path": path}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Group
def delete_group(server_url: str, auth_token: str, group_id: int) -> str:
    """
    Deletes a GitLab group by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - group_id (int): The ID of the group to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/groups/{group_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Group deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Group Members
def list_group_members(server_url: str, auth_token: str, group_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists members of a GitLab group by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - group_id (int): The ID of the group whose members to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/groups/{group_id}/members"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Group Projects
def list_group_projects(server_url: str, auth_token: str, group_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists projects of a GitLab group by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - group_id (int): The ID of the group whose projects to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/groups/{group_id}/projects"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Group Members
def manage_group_members(
    server_url: str,
    auth_token: str,
    group_id: int,
    user_id: int,
    action: str,
    access_level: int = 30,
) -> str:
    """
    Manages members of a GitLab group by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - group_id (int): The ID of the group whose members to manage.
    - user_id (int): The ID of the user to add or remove.
    - action (str): The action to perform on the member ("add", "remove").
    - access_level (int, optional): The access level for the user if action is "add". Defaults to 30 (Developer).

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/groups/{group_id}/members/{user_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"access_level": access_level}

    try:
        if action == "add":
            response = requests.post(url, headers=headers, json=payload)
        elif action == "remove":
            response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Group member managed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Group Projects
def manage_group_projects(server_url: str, auth_token: str, group_id: int, project_id: int, action: str) -> str:
    """
    Manages projects of a GitLab group by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - group_id (int): The ID of the group whose projects to manage.
    - project_id (int): The ID of the project to add or remove.
    - action (str): The action to perform on the project ("add", "remove").

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/groups/{group_id}/projects/{project_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        if action == "add":
            response = requests.post(url, headers=headers)
        elif action == "remove":
            response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Group project managed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
