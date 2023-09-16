import logging
from typing import Any, Dict, Union

import requests  # type: ignore


# List Todos
def list_todos(server_url: str, auth_token: str) -> Union[Dict[str, Any], str]:
    """
    Lists all todos for the authenticated user.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/todos"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# TODO: Implement create_todo, delete_todo

# Custom Attributes


# List Custom Attributes for Users
def list_custom_attributes_for_users(server_url: str, auth_token: str, user_id: int) -> Union[Dict[str, Any], str]:
    """
    Lists all custom attributes for a user.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user for whom to list custom attributes.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/custom_attributes"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# TODO: Implement create_custom_attribute_for_users, update_custom_attribute_for_users, delete_custom_attribute_for_users

# Container Registry


# List Container Registry Tags
def list_container_registry_tags(server_url: str, auth_token: str, project_id: int) -> Union[Dict[str, Any], str]:
    """
    Lists all container registry tags for a project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project for which to list container registry tags.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/registry/repositories/tags"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Todo
def create_todo(server_url: str, auth_token: str, project_id: int, action_name: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new todo for the authenticated user.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project for which to create a todo.
    - action_name (str): The action name for the todo (e.g., 'assigned', 'mentioned').

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/todos"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"project_id": project_id, "action_name": action_name}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Todo
def delete_todo(server_url: str, auth_token: str, todo_id: int) -> str:
    """
    Deletes a todo for the authenticated user by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - todo_id (int): The ID of the todo to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/todos/{todo_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Todo deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Custom Attribute for Users
def create_custom_attribute_for_users(
    server_url: str, auth_token: str, user_id: int, key: str, value: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new custom attribute for a user.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user for whom to create the custom attribute.
    - key (str): The key of the custom attribute.
    - value (str): The value of the custom attribute.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/custom_attributes/{key}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"value": value}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# TODO: Implement update_custom_attribute_for_users, delete_custom_attribute_for_users

# Container Registry


# Create Container Registry Tag
def create_container_registry_tag(
    server_url: str, auth_token: str, project_id: int, tag_name: str, ref: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new container registry tag for a project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project for which to create the container registry tag.
    - tag_name (str): The name of the new tag.
    - ref (str): The source to create the tag from.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/registry/repositories/tags"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"tag_name": tag_name, "ref": ref}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Container Registry Tag
def delete_container_registry_tag(server_url: str, auth_token: str, project_id: int, tag_name: str) -> str:
    """
    Deletes a container registry tag for a project by its name.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project for which to delete the container registry tag.
    - tag_name (str): The name of the tag to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/registry/repositories/tags/{tag_name}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Container registry tag deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Custom Attribute for Users
def update_custom_attribute_for_users(
    server_url: str, auth_token: str, user_id: int, key: str, value: str
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing custom attribute for a user.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user for whom to update the custom attribute.
    - key (str): The key of the custom attribute to update.
    - value (str): The new value of the custom attribute.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/custom_attributes/{key}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"value": value}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Custom Attribute for Users
def delete_custom_attribute_for_users(server_url: str, auth_token: str, user_id: int, key: str) -> str:
    """
    Deletes a custom attribute for a user by its key.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user for whom to delete the custom attribute.
    - key (str): The key of the custom attribute to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/custom_attributes/{key}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Custom attribute deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
