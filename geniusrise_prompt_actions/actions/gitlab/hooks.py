import logging
from typing import Any, Dict, Union

import requests  # type: ignore


# Create System Hook
def create_system_hook(
    server_url: str, auth_token: str, url: str, push_events: bool, tag_push_events: bool
) -> Union[Dict[str, Any], str]:
    """
    Creates a new system hook in the GitLab instance.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - url (str): The URL to which the system hook will send events.
    - push_events (bool): Whether to trigger the hook for push events.
    - tag_push_events (bool): Whether to trigger the hook for tag push events.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    api_url = f"{server_url}/api/v4/hooks"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "url": url,
        "push_events": push_events,
        "tag_push_events": tag_push_events,
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read System Hook
def read_system_hook(server_url: str, auth_token: str, hook_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a system hook in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - hook_id (int): The ID of the system hook to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/hooks/{hook_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update System Hook
def update_system_hook(
    server_url: str,
    auth_token: str,
    hook_id: int,
    url: str,
    push_events: bool,
    tag_push_events: bool,
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing system hook in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - hook_id (int): The ID of the system hook to update.
    - url (str): The new URL to which the system hook will send events.
    - push_events (bool): Whether to trigger the hook for push events.
    - tag_push_events (bool): Whether to trigger the hook for tag push events.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/hooks/{hook_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {
        "url": url,
        "push_events": push_events,
        "tag_push_events": tag_push_events,
    }

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete System Hook
def delete_system_hook(server_url: str, auth_token: str, hook_id: int) -> str:
    """
    Deletes a system hook in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - hook_id (int): The ID of the system hook to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/hooks/{hook_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "System hook deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
