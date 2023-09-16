import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# Get User Details
def get_user_details(server_url: str, auth_token: str, user_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves details of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose details to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update User Details
def update_user_details(
    server_url: str, auth_token: str, user_id: int, name: str, email: str
) -> Union[Dict[str, Any], str]:
    """
    Updates details of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose details to update.
    - name (str): The new name of the user.
    - email (str): The new email of the user.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"name": name, "email": email}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List User Projects
def list_user_projects(server_url: str, auth_token: str, user_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists projects of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose projects to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/projects"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List User SSH Keys
def list_user_ssh_keys(server_url: str, auth_token: str, user_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists SSH keys of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose SSH keys to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/keys"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List User Emails
def list_user_emails(server_url: str, auth_token: str, user_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists email addresses of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose email addresses to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/emails"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage User Projects
def manage_user_projects(
    server_url: str, auth_token: str, user_id: int, project_id: int, action: str
) -> Union[Dict[str, Any], str]:
    """
    Manages projects of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose projects to manage.
    - project_id (int): The ID of the project to manage.
    - action (str): The action to perform on the project ("add", "remove").

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/projects/{project_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        if action == "add":
            response = requests.post(url, headers=headers)
        elif action == "remove":
            response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage User SSH Keys
def manage_user_ssh_keys(server_url: str, auth_token: str, user_id: int, key_id: int, action: str) -> str:
    """
    Manages SSH keys of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose SSH keys to manage.
    - key_id (int): The ID of the SSH key to manage.
    - action (str): The action to perform on the SSH key ("add", "remove").

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/keys/{key_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        if action == "add":
            response = requests.post(url, headers=headers)
        elif action == "remove":
            response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "SSH key managed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage User Emails
def manage_user_emails(server_url: str, auth_token: str, user_id: int, email_id: int, action: str) -> str:
    """
    Manages email addresses of a GitLab user by their ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - user_id (int): The ID of the user whose email addresses to manage.
    - email_id (int): The ID of the email address to manage.
    - action (str): The action to perform on the email address ("add", "remove").

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/users/{user_id}/emails/{email_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        if action == "add":
            response = requests.post(url, headers=headers)
        elif action == "remove":
            response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Email address managed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
