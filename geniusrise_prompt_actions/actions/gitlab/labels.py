import logging
from typing import Any, Dict, Union

import requests  # type: ignore


# Create Label
def create_label(
    server_url: str, auth_token: str, project_id: int, name: str, color: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new label in a GitLab project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the label will be created.
    - name (str): The name of the label.
    - color (str): The color code of the label.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/labels"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": name, "color": color}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# TODO: Implement read_label, update_label, delete_label

# Milestones


# Create Milestone
def create_milestone(
    server_url: str,
    auth_token: str,
    project_id: int,
    title: str,
    description: str,
    due_date: str,
) -> Union[Dict[str, Any], str]:
    """
    Creates a new milestone in a GitLab project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the milestone will be created.
    - title (str): The title of the milestone.
    - description (str): The description of the milestone.
    - due_date (str): The due date of the milestone in YYYY-MM-DD format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/milestones"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"title": title, "description": description, "due_date": due_date}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Label
def read_label(server_url: str, auth_token: str, project_id: int, label_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a label in a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the label resides.
    - label_id (int): The ID of the label to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/labels/{label_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Label
def update_label(
    server_url: str,
    auth_token: str,
    project_id: int,
    label_id: int,
    name: str,
    color: str,
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing label in a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the label resides.
    - label_id (int): The ID of the label to update.
    - name (str): The new name of the label.
    - color (str): The new color code of the label.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/labels/{label_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": name, "color": color}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Label
def delete_label(server_url: str, auth_token: str, project_id: int, label_id: int) -> str:
    """
    Deletes a label in a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the label resides.
    - label_id (int): The ID of the label to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/labels/{label_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Label deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Milestone
def read_milestone(server_url: str, auth_token: str, project_id: int, milestone_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a milestone in a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the milestone resides.
    - milestone_id (int): The ID of the milestone to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/milestones/{milestone_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Milestone
def update_milestone(
    server_url: str,
    auth_token: str,
    project_id: int,
    milestone_id: int,
    title: str,
    description: str,
    due_date: str,
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing milestone in a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the milestone resides.
    - milestone_id (int): The ID of the milestone to update.
    - title (str): The new title of the milestone.
    - description (str): The new description of the milestone.
    - due_date (str): The new due date of the milestone in YYYY-MM-DD format.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/milestones/{milestone_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"title": title, "description": description, "due_date": due_date}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Milestone
def delete_milestone(server_url: str, auth_token: str, project_id: int, milestone_id: int) -> str:
    """
    Deletes a milestone in a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the milestone resides.
    - milestone_id (int): The ID of the milestone to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/milestones/{milestone_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Milestone deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
