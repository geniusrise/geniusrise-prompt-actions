import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# Create Issue
def create_issue(
    server_url: str, auth_token: str, project_id: int, title: str, description: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new issue in a GitLab project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue will be created.
    - title (str): The title of the new issue.
    - description (str): The description of the new issue.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"title": title, "description": description}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Issue
def read_issue(server_url: str, auth_token: str, project_id: int, issue_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves details of a GitLab issue by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue resides.
    - issue_id (int): The ID of the issue to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues/{issue_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Issue
def update_issue(
    server_url: str,
    auth_token: str,
    project_id: int,
    issue_id: int,
    title: str,
    description: str,
) -> Union[Dict[str, Any], str]:
    """
    Updates details of a GitLab issue by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue resides.
    - issue_id (int): The ID of the issue to update.
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


# Delete Issue
def delete_issue(server_url: str, auth_token: str, project_id: int, issue_id: int) -> str:
    """
    Deletes a GitLab issue by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue resides.
    - issue_id (int): The ID of the issue to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues/{issue_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Issue deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Issue Notes
def list_issue_notes(
    server_url: str, auth_token: str, project_id: int, issue_id: int
) -> Union[List[Dict[str, Any]], str]:
    """
    Lists notes (comments) of a GitLab issue by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue resides.
    - issue_id (int): The ID of the issue whose notes to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues/{issue_id}/notes"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Issue Labels
def list_issue_labels(
    server_url: str, auth_token: str, project_id: int, issue_id: int
) -> Union[List[Dict[str, Any]], str]:
    """
    Lists labels of a GitLab issue by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue resides.
    - issue_id (int): The ID of the issue whose labels to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues/{issue_id}/labels"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Issue Notes
def manage_issue_notes(
    server_url: str,
    auth_token: str,
    project_id: int,
    issue_id: int,
    note_id: int,
    action: str,
    body: str = "",
) -> str:
    """
    Manages notes (comments) of a GitLab issue by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue resides.
    - issue_id (int): The ID of the issue whose notes to manage.
    - note_id (int): The ID of the note to manage.
    - action (str): The action to perform on the note ("add", "update", "delete").
    - body (str, optional): The body of the note if action is "add" or "update".

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues/{issue_id}/notes/{note_id}"
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
        return "Issue note managed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Issue Labels
def manage_issue_labels(
    server_url: str, auth_token: str, project_id: int, issue_id: int, labels: List[str]
) -> Union[Dict[str, Any], str]:
    """
    Manages labels of a GitLab issue by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the issue resides.
    - issue_id (int): The ID of the issue whose labels to manage.
    - labels (List[str]): A list of labels to set for the issue.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/issues/{issue_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"labels": ",".join(labels)}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
