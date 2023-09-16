import logging
from typing import Dict, List, Union

import requests  # type: ignore


# Create Organization
def create_organization(auth_token: str, name: str, email: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - name (str): The name of the organization.
    - email (str): The email address associated with the organization.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = "https://api.github.com/orgs"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"name": name, "email": email}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Members to Organization
def add_members(auth_token: str, org: str, username: str, role: str = "member") -> str:
    """
    Adds a member to a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.
    - username (str): The GitHub username to add to the organization.
    - role (str, optional): The role to assign ("member" or "admin"). Defaults to "member".

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/memberships/{username}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"role": role}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return "Member added successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove Members from Organization
def remove_members(auth_token: str, org: str, username: str) -> str:
    """
    Removes a member from a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.
    - username (str): The GitHub username to remove from the organization.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/memberships/{username}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Member removed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Teams in Organization
def list_teams(auth_token: str, org: str) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists all the teams in a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/teams"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Teams in Organization
def manage_teams(
    auth_token: str, org: str, team_id: int, name: str, description: str, privacy: str
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Manages a team within a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.
    - team_id (int): The ID of the team to manage.
    - name (str): The name of the team.
    - description (str): The description of the team.
    - privacy (str): The privacy level of the team ("secret" or "closed").

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/teams/{team_id}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"name": name, "description": description, "privacy": privacy}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
