import logging
from typing import Dict, Union

import requests  # type: ignore


# Create Gist
def create_gist(
    auth_token: str, files: Dict[str, Dict[str, str]], description: str, public: bool
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new GitHub gist.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - files (Dict[str, Dict[str, str]]): A dictionary containing file names as keys and another dictionary with a 'content' key as values.
    - description (str): The description of the gist.
    - public (bool): Whether the gist should be public or not.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = "https://api.github.com/gists"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"files": files, "description": description, "public": public}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Gist
def read_gist(auth_token: str, gist_id: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Retrieves a GitHub gist by its ID.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - gist_id (str): The ID of the gist to retrieve.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Gist
def update_gist(
    auth_token: str, gist_id: str, files: Dict[str, Dict[str, str]], description: str
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates an existing GitHub gist.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - gist_id (str): The ID of the gist to update.
    - files (Dict[str, Dict[str, str]]): A dictionary containing file names as keys and another dictionary with a 'content' key as values.
    - description (str): The description of the gist.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"files": files, "description": description}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Gist
def delete_gist(auth_token: str, gist_id: str) -> str:
    """
    Deletes a GitHub gist.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - gist_id (str): The ID of the gist to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Gist deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Star Gist
def star_gist(auth_token: str, gist_id: str) -> str:
    """
    Stars a GitHub gist.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - gist_id (str): The ID of the gist to star.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/gists/{gist_id}/star"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.put(url, headers=headers)
        response.raise_for_status()
        return "Gist starred successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unstar Gist
def unstar_gist(auth_token: str, gist_id: str) -> str:
    """
    Unstars a GitHub gist.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - gist_id (str): The ID of the gist to unstar.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/gists/{gist_id}/star"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Gist unstarred successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Fork Gist
def fork_gist(auth_token: str, gist_id: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Forks a GitHub gist.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - gist_id (str): The ID of the gist to fork.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/gists/{gist_id}/forks"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
