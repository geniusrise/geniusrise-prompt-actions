import logging
from typing import Dict, List, Union

import requests  # type: ignore


# Search Code
def search_code(auth_token: str, query: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Searches for code across GitHub repositories.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - query (str): The search query.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/search/code?q={query}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Webhook for Repository
def create_repo_webhook(
    auth_token: str,
    owner: str,
    repo: str,
    config: Dict[str, str],
    events: List[str],
    active: bool = True,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new webhook for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - config (Dict[str, str]): The configuration for the webhook.
    - events (List[str]): The list of events the webhook will listen for.
    - active (bool, optional): Whether the webhook is active. Defaults to True.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/hooks"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"config": config, "events": events, "active": active}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Webhook for Repository
def read_repo_webhook(auth_token: str, owner: str, repo: str, hook_id: int) -> Union[Dict[str, Union[str, int]], str]:
    """
    Reads a webhook for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - hook_id (int): The ID of the webhook to read.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/hooks/{hook_id}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Webhook for Repository
def update_repo_webhook(
    auth_token: str,
    owner: str,
    repo: str,
    hook_id: int,
    config: Dict[str, str],
    events: List[str],
    active: bool = True,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates a webhook for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - hook_id (int): The ID of the webhook to update.
    - config (Dict[str, str]): The configuration for the webhook.
    - events (List[str]): The list of events the webhook will listen for.
    - active (bool, optional): Whether the webhook is active. Defaults to True.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/hooks/{hook_id}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"config": config, "events": events, "active": active}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Webhook for Repository
def delete_repo_webhook(auth_token: str, owner: str, repo: str, hook_id: int) -> str:
    """
    Deletes a webhook for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - hook_id (int): The ID of the webhook to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/hooks/{hook_id}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Webhook deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Webhook for Organization
def create_org_webhook(
    auth_token: str,
    org: str,
    config: Dict[str, str],
    events: List[str],
    active: bool = True,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new webhook for a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.
    - config (Dict[str, str]): The configuration for the webhook.
    - events (List[str]): The list of events the webhook will listen for.
    - active (bool, optional): Whether the webhook is active. Defaults to True.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/hooks"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"config": config, "events": events, "active": active}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Webhook for Organization
def read_org_webhook(auth_token: str, org: str, hook_id: int) -> Union[Dict[str, Union[str, int]], str]:
    """
    Reads a webhook for a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.
    - hook_id (int): The ID of the webhook to read.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/hooks/{hook_id}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Webhook for Organization
def update_org_webhook(
    auth_token: str,
    org: str,
    hook_id: int,
    config: Dict[str, str],
    events: List[str],
    active: bool = True,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates a webhook for a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.
    - hook_id (int): The ID of the webhook to update.
    - config (Dict[str, str]): The configuration for the webhook.
    - events (List[str]): The list of events the webhook will listen for.
    - active (bool, optional): Whether the webhook is active. Defaults to True.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/hooks/{hook_id}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"config": config, "events": events, "active": active}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Webhook for Organization
def delete_org_webhook(auth_token: str, org: str, hook_id: int) -> str:
    """
    Deletes a webhook for a GitHub organization.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The name of the organization.
    - hook_id (int): The ID of the webhook to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/orgs/{org}/hooks/{hook_id}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Webhook deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
