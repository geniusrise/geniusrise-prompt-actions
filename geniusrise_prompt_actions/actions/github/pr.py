import logging
from typing import Dict, List, Optional, Union

import requests  # type: ignore


# Create Issue
def create_issue(
    auth_token: str,
    owner: str,
    repo: str,
    title: str,
    body: Optional[str] = "",
    labels: Optional[List[str]] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - title (str): The title of the issue.
    - body (str, optional): The body text of the issue. Defaults to an empty string.
    - labels (List[str], optional): A list of labels to apply to the issue. Defaults to None.
    - assignees (List[str], optional): A list of GitHub usernames to assign the issue to. Defaults to None.
    - milestone (int, optional): The milestone number to associate with the issue. Defaults to None.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {
        "title": title,
        "body": body,
        "labels": labels,
        "assignees": assignees,
        "milestone": milestone,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Issue
def read_issue(auth_token: str, owner: str, repo: str, issue_number: int) -> Union[Dict[str, Union[str, int]], str]:
    """
    Reads an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to read.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Issue
def update_issue(
    auth_token: str,
    owner: str,
    repo: str,
    issue_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    labels: Optional[List[str]] = None,
    assignees: Optional[List[str]] = None,
    milestone: Optional[int] = None,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to update.
    - title (str, optional): The new title of the issue. Defaults to None.
    - body (str, optional): The new body text of the issue. Defaults to None.
    - state (str, optional): The new state of the issue ("open" or "closed"). Defaults to None.
    - labels (List[str], optional): A list of labels to apply to the issue. Defaults to None.
    - assignees (List[str], optional): A list of GitHub usernames to assign the issue to. Defaults to None.
    - milestone (int, optional): The milestone number to associate with the issue. Defaults to None.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {
        "title": title,
        "body": body,
        "state": state,
        "labels": labels,
        "assignees": assignees,
        "milestone": milestone,
    }

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Issues
def list_issues(
    auth_token: str,
    owner: str,
    repo: str,
    state: str = "open",
    per_page: int = 30,
    page: int = 1,
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Lists issues for a GitHub repository based on various filters.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - state (str, optional): The state of the issues to list ("open", "closed", or "all"). Defaults to "open".
    - per_page (int, optional): Number of issues per page. Defaults to 30.
    - page (int, optional): The page number to fetch. Defaults to 1.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state={state}&per_page={per_page}&page={page}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Create Pull Request
def create_pull_request(
    auth_token: str,
    owner: str,
    repo: str,
    title: str,
    body: str,
    head: str,
    base: str,
    draft: bool = False,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Creates a new pull request for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - title (str): The title of the pull request.
    - body (str): The body text of the pull request.
    - head (str): The name of the branch where your changes are implemented.
    - base (str): The name of the branch you want the changes pulled into.
    - draft (bool, optional): Whether the pull request is a draft. Defaults to False.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"title": title, "body": body, "head": head, "base": base, "draft": draft}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Pull Request
def read_pull_request(
    auth_token: str, owner: str, repo: str, pull_number: int
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Reads an existing pull request for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - pull_number (int): The number of the pull request to read.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Pull Request
def update_pull_request(
    auth_token: str,
    owner: str,
    repo: str,
    pull_number: int,
    title: Optional[str] = None,
    body: Optional[str] = None,
    state: Optional[str] = None,
    base: Optional[str] = None,
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Updates an existing pull request for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - pull_number (int): The number of the pull request to update.
    - title (str, optional): The new title of the pull request. Defaults to None.
    - body (str, optional): The new body text of the pull request. Defaults to None.
    - state (str, optional): The new state of the pull request ("open" or "closed"). Defaults to None.
    - base (str, optional): The name of the branch you want the changes pulled into. Defaults to None.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"title": title, "body": body, "state": state, "base": base}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Merge Pull Request
def merge_pull_request(
    auth_token: str,
    owner: str,
    repo: str,
    pull_number: int,
    commit_title: Optional[str] = None,
    commit_message: Optional[str] = None,
    merge_method: str = "merge",
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Merges an existing pull request for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - pull_number (int): The number of the pull request to merge.
    - commit_title (str, optional): The title for the automatic commit message. Defaults to None.
    - commit_message (str, optional): Extra detail to append to automatic commit message. Defaults to None.
    - merge_method (str, optional): The merge method to use ("merge", "squash", "rebase"). Defaults to "merge".

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/merge"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {
        "commit_title": commit_title,
        "commit_message": commit_message,
        "merge_method": merge_method,
    }

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Close Pull Request
def close_pull_request(
    auth_token: str, owner: str, repo: str, pull_number: int
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Closes an existing pull request for a GitHub repository without merging it.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - pull_number (int): The number of the pull request to close.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"state": "closed"}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Comment on Issue
def comment_on_issue(
    auth_token: str, owner: str, repo: str, issue_number: int, body: str
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Comments on an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to comment on.
    - body (str): The body text of the comment.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"body": body}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Comment on Pull Request
def comment_on_pull_request(
    auth_token: str, owner: str, repo: str, pull_number: int, body: str
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Comments on an existing pull request for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - pull_number (int): The number of the pull request to comment on.
    - body (str): The body text of the comment.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pull_number}/comments"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"body": body}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Labels to Issue
def add_labels(
    auth_token: str, owner: str, repo: str, issue_number: int, labels: List[str]
) -> Union[List[Dict[str, Union[str, int]]], str]:
    """
    Adds labels to an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to add labels to.
    - labels (List[str]): A list of labels to add to the issue.

    Returns:
    - Union[List[Dict[str, Union[str, int]]], str]: A list of dictionaries containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"labels": labels}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove Labels from Issue
def remove_labels(auth_token: str, owner: str, repo: str, issue_number: int) -> str:
    """
    Removes all labels from an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to remove labels from.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/labels"
    headers = {"Authorization": f"token {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Labels removed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Assignees to Issue
def add_assignees(
    auth_token: str, owner: str, repo: str, issue_number: int, assignees: List[str]
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Adds assignees to an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to add assignees to.
    - assignees (List[str]): A list of GitHub usernames to assign to the issue.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/assignees"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"assignees": assignees}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove Assignees from Issue
def remove_assignees(auth_token: str, owner: str, repo: str, issue_number: int, assignees: List[str]) -> str:
    """
    Removes assignees from an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to remove assignees from.
    - assignees (List[str]): A list of GitHub usernames to unassign from the issue.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/assignees"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"assignees": assignees}

    try:
        response = requests.delete(url, headers=headers, json=payload)
        response.raise_for_status()
        return "Assignees removed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Milestone to Issue
def add_milestone(
    auth_token: str, owner: str, repo: str, issue_number: int, milestone_number: int
) -> Union[Dict[str, Union[str, int]], str]:
    """
    Adds a milestone to an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to add a milestone to.
    - milestone_number (int): The number of the milestone to associate with the issue.

    Returns:
    - Union[Dict[str, Union[str, int]], str]: A dictionary containing the response from GitHub API or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"milestone": milestone_number}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove Milestone from Issue
def remove_milestone(auth_token: str, owner: str, repo: str, issue_number: int) -> str:
    """
    Removes a milestone from an existing issue for a GitHub repository.

    Parameters:
    - auth_token (str): The authentication token for GitHub API.
    - owner (str): The owner of the repository.
    - repo (str): The name of the repository.
    - issue_number (int): The number of the issue to remove a milestone from.

    Returns:
    - str: A success message or an error message.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {auth_token}"}
    payload = {"milestone": None}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return "Milestone removed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
