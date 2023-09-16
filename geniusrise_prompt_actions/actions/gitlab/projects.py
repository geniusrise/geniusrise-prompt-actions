import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# Create Project
def create_project(
    server_url: str,
    auth_token: str,
    name: str,
    description: str = "",
    visibility: str = "private",
) -> Union[Dict[str, Any], str]:
    """
    Creates a new GitLab project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - name (str): The name of the project.
    - description (str, optional): The description of the project. Defaults to an empty string.
    - visibility (str, optional): The visibility level of the project ("private", "internal", "public"). Defaults to "private".

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": name, "description": description, "visibility": visibility}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Project
def read_project(server_url: str, auth_token: str, project_id: int) -> Union[Dict[str, Any], str]:
    """
    Reads a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Project
def update_project(
    server_url: str,
    auth_token: str,
    project_id: int,
    name: str,
    description: str = "",
    visibility: str = "private",
) -> Union[Dict[str, Any], str]:
    """
    Updates a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project to update.
    - name (str): The new name of the project.
    - description (str, optional): The new description of the project. Defaults to an empty string.
    - visibility (str, optional): The new visibility level of the project ("private", "internal", "public"). Defaults to "private".

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": name, "description": description, "visibility": visibility}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Project
def delete_project(server_url: str, auth_token: str, project_id: int) -> str:
    """
    Deletes a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Project deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Fork Project
def fork_project(server_url: str, auth_token: str, project_id: int) -> Union[Dict[str, Any], str]:
    """
    Forks a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project to fork.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/fork"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Project Members
def list_project_members(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists members of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose members to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/members"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Project Members
def manage_project_members(
    server_url: str, auth_token: str, project_id: int, user_id: int, access_level: int
) -> Union[Dict[str, Any], str]:
    """
    Manages members of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose members to manage.
    - user_id (int): The ID of the user to add or update in the project.
    - access_level (int): The access level to assign to the user (e.g., 10 for guest, 20 for reporter).

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/members"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"user_id": user_id, "access_level": access_level}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Project Hooks
def list_project_hooks(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists hooks of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose hooks to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/hooks"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Project Hooks
def manage_project_hooks(
    server_url: str, auth_token: str, project_id: int, hook_url: str, events: List[str]
) -> Union[Dict[str, Any], str]:
    """
    Manages hooks of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose hooks to manage.
    - hook_url (str): The URL to which the hook should post data.
    - events (List[str]): The events that should trigger the hook (e.g., ["push", "issues"]).

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/hooks"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "url": hook_url,
        "push_events": "push" in events,
        "issues_events": "issues" in events,
        "merge_requests_events": "merge_requests" in events,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Project Issues
def list_project_issues(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists issues of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose issues to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Project Issues
def manage_project_issues(
    server_url: str,
    auth_token: str,
    project_id: int,
    issue_id: int,
    title: str,
    description: str,
) -> Union[Dict[str, Any], str]:
    """
    Manages issues of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose issues to manage.
    - issue_id (int): The ID of the issue to manage.
    - title (str): The new title of the issue.
    - description (str): The new description of the issue.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues/{issue_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"title": title, "description": description}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Project Merge Requests
def list_project_merge_requests(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists merge requests of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose merge requests to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Project Merge Requests
def manage_project_merge_requests(
    server_url: str,
    auth_token: str,
    project_id: int,
    merge_request_id: int,
    title: str,
    description: str,
) -> Union[Dict[str, Any], str]:
    """
    Manages merge requests of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose merge requests to manage.
    - merge_request_id (int): The ID of the merge request to manage.
    - title (str): The new title of the merge request.
    - description (str): The new description of the merge request.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"title": title, "description": description}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
