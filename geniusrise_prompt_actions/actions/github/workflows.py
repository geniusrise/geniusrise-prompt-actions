import base64
import logging
from typing import Dict, List, Union

import requests  # type: ignore


# List Workflows for Repository
def list_workflows(auth_token: str, owner: str, repo: str) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists all GitHub Actions workflows for a repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Workflow for Repository
def create_workflow(
    auth_token: str, owner: str, repo: str, workflow_content: str, path: str
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new GitHub Actions workflow for a repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - workflow_content (str): The content of the workflow file.
    - path (str): The path where the workflow file will be created.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {
        "message": "Create GitHub Actions workflow",
        "content": base64.b64encode(workflow_content.encode()).decode(),
        "branch": "main",
    }

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Workflow for Repository
def manage_workflow(
    auth_token: str, owner: str, repo: str, workflow_id: int, state: str
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Manages a GitHub Actions workflow for a repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - workflow_id (int): The ID of the workflow to manage.
    - state (str): The state to set for the workflow ("active" or "disabled").

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/actions/workflows/{workflow_id}/enable"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"state": state}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
