import logging
from typing import Dict, List, Any, Union

import requests  # type: ignore


# Create Component
def create_component(
    server_url: str, auth: Dict[str, str], project_id: str, name: str, description: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new component in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - project_id (str): The ID or key of the project where the component will be created.
    - name (str): The name of the new component.
    - description (str): The description of the component.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/component"
    headers = {"Content-Type": "application/json"}
    payload = {"name": name, "description": description, "project": project_id}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Component
def read_component(server_url: str, auth: Dict[str, str], component_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves a component from Jira by its ID.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - component_id (str): The ID of the component to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/component/{component_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Component
def update_component(
    server_url: str, auth: Dict[str, str], component_id: str, new_name: str, new_description: str
) -> Union[Dict[str, Any], str]:
    """
    Updates a component's details in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - component_id (str): The ID of the component to update.
    - new_name (str): The new name for the component.
    - new_description (str): The new description for the component.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/component/{component_id}"
    headers = {"Content-Type": "application/json"}
    payload = {"name": new_name, "description": new_description}

    try:
        response = requests.put(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Component
def delete_component(server_url: str, auth: Dict[str, str], component_id: str) -> str:
    """
    Deletes a component from Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - component_id (str): The ID of the component to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/component/{component_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Component deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Components
def list_all_components(server_url: str, auth: Dict[str, str], project_id: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all components in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - project_id (str): The ID or key of the project for which to list components.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the components or an error message.
    """
    url = f"{server_url}/rest/api/2/project/{project_id}/components"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
