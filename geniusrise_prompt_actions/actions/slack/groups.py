import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# Create User Group
def create_user_group(token: str, name: str, description: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new user group in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - name (str): The name of the new user group.
    - description (str): A description for the new user group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/usergroups.create"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"name": name, "description": description}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update User Group
def update_user_group(token: str, user_group_id: str, name: str, description: str) -> Union[Dict[str, Any], str]:
    """
    Updates an existing user group in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - user_group_id (str): The ID of the user group to update.
    - name (str): The new name for the user group.
    - description (str): A new description for the user group.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/usergroups.update"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"usergroup": user_group_id, "name": name, "description": description}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Disable User Group
def disable_user_group(token: str, user_group_id: str) -> Union[Dict[str, Any], str]:
    """
    Disables a user group in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - user_group_id (str): The ID of the user group to disable.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/usergroups.disable"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"usergroup": user_group_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Enable User Group
def enable_user_group(token: str, user_group_id: str) -> Union[Dict[str, Any], str]:
    """
    Enables a user group in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - user_group_id (str): The ID of the user group to enable.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/usergroups.enable"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"usergroup": user_group_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List User Groups
def list_user_groups(token: str) -> Union[Dict[str, Any], str]:
    """
    Lists all user groups in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/usergroups.list"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
