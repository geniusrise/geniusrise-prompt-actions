import logging
from typing import Dict, List, Optional, Union

import requests  # type: ignore


def create_repository(
    auth_token: str,
    name: str,
    description: Optional[str] = "",
    private: bool = False,
    organization: Optional[str] = None,
) -> Dict[str, Union[str, int]]:
    """
    Creates a new GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - name (str): The name of the repository.
    - description (str, optional): The description of the repository. Defaults to an empty string.
    - private (bool, optional): Whether the repository should be private. Defaults to False.
    - organization (str, optional): The organization under which to create the repository. If None, creates under authenticated user.

    Returns:
    - Dict[str, Union[str, int]]: A dictionary containing the response from GitHub API.

    Usage:
    >>> create_repository(auth_token="your_token_here", name="my-repo", description="My new repo", private=True)
    """
    url = f"https://api.github.com/{'orgs/' + organization if organization else 'user'}/repos"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"name": name, "description": description, "private": private}

    response = requests.post(url, headers=headers, json=payload)
    return response.json()


def delete_repository(auth_token: str, owner: str, repo: str) -> Dict[str, Union[str, int]]:
    """
    Deletes a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository to delete.

    Returns:
    - Dict[str, Union[str, int]]: A dictionary containing the response from GitHub API.

    Usage:
    >>> delete_repository(auth_token="your_token_here", owner="your_username", repo="repo_to_delete")
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {auth_token}"}

    response = requests.delete(url, headers=headers)
    return response.json()


def update_repository(
    auth_token: str,
    owner: str,
    repo: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    private: Optional[bool] = None,
) -> Dict[str, Union[str, int]]:
    """
    Updates the details of an existing GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository to update.
    - name (str, optional): The new name of the repository.
    - description (str, optional): The new description of the repository.
    - private (bool, optional): Whether the repository should be private.

    Returns:
    - Dict[str, Union[str, int]]: A dictionary containing the response from GitHub API.

    Usage:
    >>> update_repository(auth_token="your_token_here", owner="your_username", repo="repo_to_update", name="new_name")
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"name": name, "description": description, "private": private}

    # Remove None values from payload
    payload = {k: v for k, v in payload.items() if v is not None}

    response = requests.patch(url, headers=headers, json=payload)
    return response.json()


def list_user_repositories(
    auth_token: str,
    username: str,
    sort: Optional[str] = "created",
    per_page: int = 30,
    page: int = 1,
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists repositories for a specific user with pagination.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - username (str): The username whose repositories to list.
    - sort (str, optional): The sort order for repositories. Can be "created", "updated", or "pushed". Defaults to "created".
    - per_page (int, optional): Number of repositories per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.

    Usage:
    >>> list_user_repositories(auth_token="your_token_here", username="some_username", per_page=10, page=2)
    """
    url = f"https://api.github.com/users/{username}/repos?sort={sort}&per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


def list_organization_repositories(
    auth_token: str,
    org: str,
    sort: Optional[str] = "created",
    per_page: int = 30,
    page: int = 1,
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists repositories for a specific organization with pagination.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - org (str): The organization whose repositories to list.
    - sort (str, optional): The sort order for repositories. Can be "created", "updated", or "pushed". Defaults to "created".
    - per_page (int, optional): Number of repositories per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.

    Usage:
    >>> list_organization_repositories(auth_token="your_token_here", org="some_organization", per_page=10, page=2)
    """
    url = f"https://api.github.com/orgs/{org}/repos?sort={sort}&per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Fork Repository
def fork_repository(
    auth_token: str, owner: str, repo: str, organization: Optional[str] = None
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Forks a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository to fork.
    - repo (str): The name of the repository to fork.
    - organization (str, optional): The organization under which to create the fork. If None, creates under authenticated user.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/forks"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"organization": organization} if organization else {}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Star Repository
def star_repository(auth_token: str, owner: str, repo: str) -> str:
    """
    Stars a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository to star.
    - repo (str): The name of the repository to star.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/user/starred/{owner}/{repo}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.put(url, headers=headers)
        response.raise_for_status()
        return "Successfully starred the repository."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unstar Repository
def unstar_repository(auth_token: str, owner: str, repo: str) -> str:
    """
    Unstars a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository to unstar.
    - repo (str): The name of the repository to unstar.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/user/starred/{owner}/{repo}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Successfully unstarred the repository."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Starred Repositories
def list_starred_repositories(
    auth_token: str, per_page: int = 30, page: int = 1
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists repositories that the authenticated user has starred.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - per_page (int, optional): Number of repositories per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/user/starred?per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Watch Repository
def watch_repository(auth_token: str, owner: str, repo: str) -> str:
    """
    Watches a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository to watch.
    - repo (str): The name of the repository to watch.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/subscription"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"subscribed": True}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return "Successfully watched the repository."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unwatch Repository
def unwatch_repository(auth_token: str, owner: str, repo: str) -> str:
    """
    Unwatches a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository to unwatch.
    - repo (str): The name of the repository to unwatch.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/subscription"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Successfully unwatched the repository."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Repository Topics
def get_repository_topics(auth_token: str, owner: str, repo: str) -> Union[List[str], str]:
    """
    Gets the topics of a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.

    Returns:
    - Union[List[str], str]: A list of topics or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/topics"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.mercy-preview+json",
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json().get("names", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Set Repository Topics
def set_repository_topics(auth_token: str, owner: str, repo: str, topics: List[str]) -> Union[List[str], str]:
    """
    Sets the topics of a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - topics (List[str]): A list of topics to set for the repository.

    Returns:
    - Union[List[str], str]: A list of topics or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/topics"
    headers = {
        "Authorization": f"token {auth_token}",
        "Accept": "application/vnd.github.mercy-preview+json",
    }
    payload = {"names": topics}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("names", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Releases
def list_releases(
    auth_token: str, owner: str, repo: str, per_page: int = 30, page: int = 1
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists releases for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - per_page (int, optional): Number of releases per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/releases?per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Release
def create_release(
    auth_token: str,
    owner: str,
    repo: str,
    tag_name: str,
    name: str,
    body: str,
    draft: bool = False,
    prerelease: bool = False,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new release for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - tag_name (str): The name of the tag for the release.
    - name (str): The name of the release.
    - body (str): The description of the release.
    - draft (bool, optional): Whether the release is a draft. Defaults to False.
    - prerelease (bool, optional): Whether the release is a prerelease. Defaults to False.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/releases"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {
        "tag_name": tag_name,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Release
def update_release(
    auth_token: str,
    owner: str,
    repo: str,
    release_id: int,
    tag_name: str,
    name: str,
    body: str,
    draft: bool = False,
    prerelease: bool = False,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates an existing release for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - release_id (int): The ID of the release to update.
    - tag_name (str): The name of the tag for the release.
    - name (str): The name of the release.
    - body (str): The description of the release.
    - draft (bool, optional): Whether the release is a draft. Defaults to False.
    - prerelease (bool, optional): Whether the release is a prerelease. Defaults to False.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/{release_id}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {
        "tag_name": tag_name,
        "name": name,
        "body": body,
        "draft": draft,
        "prerelease": prerelease,
    }

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Release
def delete_release(auth_token: str, owner: str, repo: str, release_id: int) -> str:
    """
    Deletes a release for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - release_id (int): The ID of the release to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/releases/{release_id}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Successfully deleted the release."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Tags
def list_tags(
    auth_token: str, owner: str, repo: str, per_page: int = 30, page: int = 1
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists tags for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - per_page (int, optional): Number of tags per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/tags?per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Tag
def create_tag(
    auth_token: str,
    owner: str,
    repo: str,
    tag: str,
    message: str,
    object: str,
    type: str = "commit",
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new tag for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - tag (str): The name of the tag to create.
    - message (str): The message associated with the tag.
    - object (str): The SHA of the git object this is tagging.
    - type (str, optional): The type of the object we're tagging. Defaults to "commit".

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/git/tags"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"tag": tag, "message": message, "object": object, "type": type}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Tag
# GitHub API does not provide a direct way to delete a tag. You have to delete the reference to the tag.
def delete_tag(auth_token: str, owner: str, repo: str, tag: str) -> str:
    """
    Deletes a tag for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - tag (str): The name of the tag to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/git/refs/tags/{tag}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Successfully deleted the tag."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
