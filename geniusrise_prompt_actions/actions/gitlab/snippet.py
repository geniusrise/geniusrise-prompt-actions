import logging
from typing import Any, Dict, Union

import requests  # type: ignore


# Create Snippet
def create_snippet(
    server_url: str,
    auth_token: str,
    title: str,
    file_name: str,
    content: str,
    visibility: str,
) -> Union[Dict[str, Any], str]:
    """
    Creates a new snippet in the GitLab instance.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - title (str): The title of the snippet.
    - file_name (str): The name of the file in the snippet.
    - content (str): The content of the snippet.
    - visibility (str): The visibility level of the snippet ('private', 'internal', 'public').

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/snippets"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "title": title,
        "file_name": file_name,
        "content": content,
        "visibility": visibility,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Snippet
def read_snippet(server_url: str, auth_token: str, snippet_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a snippet in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - snippet_id (int): The ID of the snippet to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/snippets/{snippet_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Snippet
def update_snippet(
    server_url: str,
    auth_token: str,
    snippet_id: int,
    title: str,
    file_name: str,
    content: str,
    visibility: str,
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing snippet in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - snippet_id (int): The ID of the snippet to update.
    - title (str): The new title of the snippet.
    - file_name (str): The new name of the file in the snippet.
    - content (str): The new content of the snippet.
    - visibility (str): The new visibility level of the snippet ('private', 'internal', 'public').

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/snippets/{snippet_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "title": title,
        "file_name": file_name,
        "content": content,
        "visibility": visibility,
    }

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Snippet
def delete_snippet(server_url: str, auth_token: str, snippet_id: int) -> str:
    """
    Deletes a snippet in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - snippet_id (int): The ID of the snippet to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/snippets/{snippet_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Snippet deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
