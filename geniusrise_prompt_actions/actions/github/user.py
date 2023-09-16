import logging
from typing import Dict, List, Optional, Union

import requests  # type: ignore


# Get User Details
def get_user_details(auth_token: str, username: str) -> Union[Dict[str, Union[str, int]], str]:
    """
    Retrieves details of a GitHub user.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - username (str): The GitHub username of the user whose details are to be retrieved.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update User Profile
def update_user_profile(
    auth_token: str,
    name: Optional[str] = None,
    email: Optional[str] = None,
    bio: Optional[str] = None,
    location: Optional[str] = None,
    hireable: Optional[bool] = None,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates the authenticated user's GitHub profile.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - name (str, optional): The name of the user. Defaults to None.
    - email (str, optional): The email of the user. Defaults to None.
    - bio (str, optional): The bio of the user. Defaults to None.
    - location (str, optional): The location of the user. Defaults to None.
    - hireable (bool, optional): Whether the user is hireable. Defaults to None.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = "https://api.github.com/user"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {
        "name": name,
        "email": email,
        "bio": bio,
        "location": location,
        "hireable": hireable,
    }

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Followers
def list_followers(
    auth_token: str, username: str, per_page: int = 30, page: int = 1
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists the followers of a GitHub user.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - username (str): The GitHub username whose followers are to be listed.
    - per_page (int, optional): Number of followers per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/users/{username}/followers?per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Following
def list_following(
    auth_token: str, username: str, per_page: int = 30, page: int = 1
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists the users that a GitHub user is following.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - username (str): The GitHub username whose following list is to be retrieved.
    - per_page (int, optional): Number of users to list per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/users/{username}/following?per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Follow User
def follow_user(auth_token: str, username: str) -> str:
    """
    Follows a GitHub user.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - username (str): The GitHub username to follow.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/user/following/{username}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.put(url, headers=headers)
        response.raise_for_status()
        return "User followed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unfollow User
def unfollow_user(auth_token: str, username: str) -> str:
    """
    Unfollows a GitHub user.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - username (str): The GitHub username to unfollow.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/user/following/{username}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "User unfollowed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
