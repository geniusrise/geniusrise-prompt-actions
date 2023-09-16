import logging
from typing import Dict, Union

import requests  # type: ignore


# Create Project
def create_project(
    auth_token: str, owner: str, repo: str, name: str, body: str
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new GitHub project.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - name (str): The name of the project.
    - body (str): The description of the project.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/projects"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    payload = {"name": name, "body": body}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Project
def read_project(auth_token: str, project_id: int) -> Union[Dict[str, Union[str, int]], str]:
    """
    Reads a GitHub project by its ID.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - project_id (int): The ID of the project to read.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/projects/{project_id}"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Project
def update_project(auth_token: str, project_id: int, name: str, body: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates a GitHub project by its ID.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - project_id (int): The ID of the project to update.
    - name (str): The new name of the project.
    - body (str): The new description of the project.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/projects/{project_id}"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    payload = {"name": name, "body": body}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Project
def delete_project(auth_token: str, project_id: int) -> str:
    """
    Deletes a GitHub project by its ID.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - project_id (int): The ID of the project to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/projects/{project_id}"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Project deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Project Column
def add_project_column(auth_token: str, project_id: int, name: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Adds a new column to a GitHub project.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - project_id (int): The ID of the project to which the column will be added.
    - name (str): The name of the column.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/projects/{project_id}/columns"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    payload = {"name": name}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Project Column
def manage_project_column(auth_token: str, column_id: int, name: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates the name of a GitHub project column.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - column_id (int): The ID of the column to manage.
    - name (str): The new name of the column.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/projects/columns/{column_id}"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    payload = {"name": name}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Project Card
def add_project_card(auth_token: str, column_id: int, note: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Adds a new card to a GitHub project column.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - column_id (int): The ID of the column to which the card will be added.
    - note (str): The note or content of the card.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/projects/columns/{column_id}/cards"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    payload = {"note": note}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Project Card
def manage_project_card(auth_token: str, card_id: int, note: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates the note or content of a GitHub project card.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - card_id (int): The ID of the card to manage.
    - note (str): The new note or content of the card.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/projects/columns/cards/{card_id}"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    payload = {"note": note}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
