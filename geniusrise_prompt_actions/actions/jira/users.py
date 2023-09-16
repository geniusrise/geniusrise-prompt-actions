import logging
from typing import Dict, List, Any, Union

import requests  # type: ignore


# Create Project
def create_project(
    server_url: str, auth: Dict[str, str], name: str, project_type: str, description: str = ""
) -> Union[Dict[str, Any], str]:
    """
    Creates a new Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - name (str): The name of the project.
    - project_type (str): The project type, e.g. "software".
    - description (str, optional): The description of the project. Defaults to an empty string.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/project"
    headers = {"Content-Type": "application/json"}
    payload = {
        "name": name,
        "projectType": {"id": project_type},
        "description": description,
    }

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Project
def read_project(server_url: str, auth: Dict[str, str], project_key: str) -> Union[Dict[str, Any], str]:
    """
    Reads a Jira project by its key.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - project_key (str): The key of the project to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/project/{project_key}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Project
def update_project(
    server_url: str,
    auth: Dict[str, str],
    project_key: str,
    name: str,
    project_type: str,
    description: str = "",
) -> Union[Dict[str, Any], str]:
    """
    Updates a Jira project by its key.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - project_key (str): The key of the project to update.
    - name (str): The new name of the project.
    - project_type (str): The new project type, e.g. "software".
    - description (str, optional): The new description of the project. Defaults to an empty string.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/project/{project_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "name": name,
        "projectType": {"id": project_type},
        "description": description,
    }

    try:
        response = requests.put(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Project
def delete_project(server_url: str, auth: Dict[str, str], project_key: str) -> str:
    """
    Deletes a Jira project by its key.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - project_key (str): The key of the project to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/project/{project_key}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Project deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Projects
def list_projects(server_url: str, auth: Dict[str, str]) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all Jira projects.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the project details or an error message.
    """
    url = "{server_url}/rest/api/2/project"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        projects = response.json()["values"]
        return projects
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
