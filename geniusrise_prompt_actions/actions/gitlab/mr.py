import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# Create Merge Request
def create_merge_request(
    server_url: str,
    auth_token: str,
    project_id: int,
    source_branch: str,
    target_branch: str,
    title: str,
) -> Union[Dict[str, Any], str]:
    """
    Creates a new merge request in a GitLab project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the merge request will be created.
    - source_branch (str): The source branch for the merge request.
    - target_branch (str): The target branch for the merge request.
    - title (str): The title of the new merge request.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "source_branch": source_branch,
        "target_branch": target_branch,
        "title": title,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Merge Request
def read_merge_request(
    server_url: str, auth_token: str, project_id: int, merge_request_id: int
) -> Union[Dict[str, Any], str]:
    """
    Retrieves details of a GitLab merge request by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the merge request resides.
    - merge_request_id (int): The ID of the merge request to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Merge Request
def update_merge_request(
    server_url: str,
    auth_token: str,
    project_id: int,
    merge_request_id: int,
    title: str,
    description: str,
) -> Union[Dict[str, Any], str]:
    """
    Updates details of a GitLab merge request by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the merge request resides.
    - merge_request_id (int): The ID of the merge request to update.
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


# Delete Merge Request
def delete_merge_request(server_url: str, auth_token: str, project_id: int, merge_request_id: int) -> str:
    """
    Deletes a GitLab merge request by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the merge request resides.
    - merge_request_id (int): The ID of the merge request to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Merge request deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Merge Request Notes
def list_merge_request_notes(
    server_url: str, auth_token: str, project_id: int, merge_request_id: int
) -> Union[List[Dict[str, Any]], str]:
    """
    Lists notes (comments) of a GitLab merge request by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the merge request resides.
    - merge_request_id (int): The ID of the merge request whose notes to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}/notes"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Merge Request Commits
def list_merge_request_commits(
    server_url: str, auth_token: str, project_id: int, merge_request_id: int
) -> Union[List[Dict[str, Any]], str]:
    """
    Lists commits of a GitLab merge request by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the merge request resides.
    - merge_request_id (int): The ID of the merge request whose commits to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}/commits"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Merge Request Notes
def manage_merge_request_notes(
    server_url: str,
    auth_token: str,
    project_id: int,
    merge_request_id: int,
    note_id: int,
    action: str,
    body: str = "",
) -> str:
    """
    Manages notes (comments) of a GitLab merge request by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the merge request resides.
    - merge_request_id (int): The ID of the merge request whose notes to manage.
    - note_id (int): The ID of the note to manage.
    - action (str): The action to perform on the note ("add", "update", "delete").
    - body (str, optional): The body of the note if action is "add" or "update".

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/merge_requests/{merge_request_id}/notes/{note_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"body": body}

    try:
        if action == "add":
            response = requests.post(url, headers=headers, json=payload)
        elif action == "update":
            response = requests.put(url, headers=headers, json=payload)
        elif action == "delete":
            response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Merge request note managed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
