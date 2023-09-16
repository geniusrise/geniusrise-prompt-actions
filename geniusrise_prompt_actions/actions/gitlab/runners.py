import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# List Runners
def list_runners(server_url: str, auth_token: str) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all runners available in the GitLab instance.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/runners"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Runner
def create_runner(
    server_url: str,
    auth_token: str,
    description: str,
    active: bool,
    tag_list: List[str],
) -> Union[Dict[str, Any], str]:
    """
    Creates a new runner in the GitLab instance.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - description (str): The description of the runner.
    - active (bool): Whether the runner is active.
    - tag_list (List[str]): The list of tags for the runner.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/runners"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"description": description, "active": active, "tag_list": tag_list}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Runner
def delete_runner(server_url: str, auth_token: str, runner_id: int) -> str:
    """
    Deletes a runner from the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - runner_id (int): The ID of the runner to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/runners/{runner_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Runner deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Enable Runner
def enable_runner(server_url: str, auth_token: str, runner_id: int) -> str:
    """
    Enables a runner in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - runner_id (int): The ID of the runner to enable.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/runners/{runner_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"active": True}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return "Runner enabled successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Disable Runner
def disable_runner(server_url: str, auth_token: str, runner_id: int) -> str:
    """
    Disables a runner in the GitLab instance by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - runner_id (int): The ID of the runner to disable.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/runners/{runner_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"active": False}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return "Runner disabled successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
