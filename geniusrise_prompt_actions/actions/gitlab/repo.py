import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# List Branches
def list_branches(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists branches of a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose branches to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/branches"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Branch
def create_branch(
    server_url: str, auth_token: str, project_id: int, branch_name: str, ref: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new branch in a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the branch will be created.
    - branch_name (str): The name of the new branch.
    - ref (str): The name of the branch or tag to fork from.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/branches"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"branch": branch_name, "ref": ref}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Branch
def delete_branch(server_url: str, auth_token: str, project_id: int, branch_name: str) -> str:
    """
    Deletes a branch in a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the branch will be deleted.
    - branch_name (str): The name of the branch to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/branches/{branch_name}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Branch deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Tags
def list_tags(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists tags of a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose tags to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/tags"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Tag
def create_tag(
    server_url: str,
    auth_token: str,
    project_id: int,
    tag_name: str,
    ref: str,
    message: str = "",
) -> Union[Dict[str, Any], str]:
    """
    Creates a new tag in a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the tag will be created.
    - tag_name (str): The name of the new tag.
    - ref (str): The name of the branch or commit to tag from.
    - message (str, optional): The message for the tag. Defaults to an empty string.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/tags"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"tag_name": tag_name, "ref": ref, "message": message}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Tag
def delete_tag(server_url: str, auth_token: str, project_id: int, tag_name: str) -> str:
    """
    Deletes a tag in a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the tag will be deleted.
    - tag_name (str): The name of the tag to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/tags/{tag_name}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Tag deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Commits
def list_commits(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists commits of a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose commits to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/commits"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Repository Files
def list_repository_files(
    server_url: str, auth_token: str, project_id: int, path: str = ""
) -> Union[List[Dict[str, Any]], str]:
    """
    Lists files in a GitLab repository by its project ID and path.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose files to list.
    - path (str, optional): The path within the repository to list files from. Defaults to the root directory.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/tree"
    headers = {"Authorization": f"Bearer {auth_token}"}
    params = {"path": path} if path else {}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Commits
def manage_commits(
    server_url: str, auth_token: str, project_id: int, commit_sha: str, action: str
) -> Union[Dict[str, Any], str]:
    """
    Manages commits of a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose commits to manage.
    - commit_sha (str): The SHA of the commit to manage.
    - action (str): The action to perform on the commit ("cherry_pick", "revert").

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/commits/{commit_sha}/{action}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Repository Files
def manage_repository_files(
    server_url: str,
    auth_token: str,
    project_id: int,
    file_path: str,
    action: str,
    content: str = "",
    commit_message: str = "",
) -> Union[Dict[str, Any], str]:
    """
    Manages files in a GitLab repository by its project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose files to manage.
    - file_path (str): The path of the file to manage.
    - action (str): The action to perform on the file ("create", "update", "delete").
    - content (str, optional): The content for the file if action is "create" or "update". Defaults to an empty string.
    - commit_message (str, optional): The commit message. Defaults to an empty string.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/repository/files/{file_path}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"action": action, "content": content, "commit_message": commit_message}

    try:
        if action == "delete":
            response = requests.delete(url, headers=headers, json=payload)
        else:
            response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
