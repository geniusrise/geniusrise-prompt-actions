import logging
from typing import Dict, List, Any, Union, Optional

import requests  # type: ignore


def create_issue(
    server_url: str, auth: Dict[str, str], project_key: str, issue_type: str, summary: str, description: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new issue in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - project_key (str): The key of the project where the issue will be created.
    - issue_type (str): The type of the issue (e.g., 'Bug', 'Task').
    - summary (str): The summary of the issue.
    - description (str): The description of the issue.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/issue"
    headers = {"Content-Type": "application/json"}
    payload = {
        "fields": {
            "project": {"key": project_key},
            "issuetype": {"name": issue_type},
            "summary": summary,
            "description": description,
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Issue
def read_issue(server_url: str, auth: Dict[str, str], issue_key: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves an issue from a Jira project by its key.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue to retrieve (e.g., 'PROJ-123').

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


def update_issue(
    server_url: str, auth: Dict[str, str], issue_key: str, fields: Dict[str, Any]
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing issue in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue to update (e.g., 'PROJ-123').
    - fields (Dict[str, Any]): A dictionary containing the fields to update.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}"
    headers = {"Content-Type": "application/json"}
    payload = {"fields": fields}

    try:
        response = requests.put(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Issue
def delete_issue(server_url: str, auth: Dict[str, str], issue_key: str) -> str:
    """
    Deletes an issue from a Jira project by its key.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue to delete (e.g., 'PROJ-123').

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Issue deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Issues by Filter
def list_issues_by_filter(
    server_url: str, auth: Dict[str, str], jql: str, fields: Optional[List[str]] = None
) -> Union[Dict[str, Any], str]:
    """
    Lists issues in a Jira project based on a JQL filter.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - jql (str): The JQL query string to filter issues.
    - fields (List[str]): A list of fields to return for each issue (optional).

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/search"
    headers = {"Content-Type": "application/json"}
    params = {"jql": jql, "fields": fields if fields else "summary,key"}

    try:
        response = requests.get(url, headers=headers, params=params, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Comment to Issue
def add_comment_to_issue(
    server_url: str, auth: Dict[str, str], issue_key: str, comment: str
) -> Union[Dict[str, Any], str]:
    """
    Adds a comment to an issue in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue to which the comment will be added (e.g., 'PROJ-123').
    - comment (str): The comment text.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}/comment"
    headers = {"Content-Type": "application/json"}
    payload = {"body": comment}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Comment in Issue
def update_comment_in_issue(
    server_url: str, auth: Dict[str, str], issue_key: str, comment_id: str, new_comment: str
) -> Union[Dict[str, Any], str]:
    """
    Updates a comment in an issue in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue containing the comment (e.g., 'PROJ-123').
    - comment_id (str): The ID of the comment to update.
    - new_comment (str): The new comment text.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}/comment/{comment_id}"
    headers = {"Content-Type": "application/json"}
    payload = {"body": new_comment}

    try:
        response = requests.put(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Comment from Issue
def delete_comment_from_issue(server_url: str, auth: Dict[str, str], issue_key: str, comment_id: str) -> str:
    """
    Deletes a comment from an issue in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue containing the comment (e.g., 'PROJ-123').
    - comment_id (str): The ID of the comment to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}/comment/{comment_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Comment deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Add Attachment to Issue
def add_attachment_to_issue(
    server_url: str, auth: Dict[str, str], issue_key: str, file_path: str
) -> Union[Dict[str, Any], str]:
    """
    Adds an attachment to an issue in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue to which the attachment will be added (e.g., 'PROJ-123').
    - file_path (str): The local file path of the attachment.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}/attachments"
    headers = {"X-Atlassian-Token": "no-check"}

    try:
        with open(file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(url, headers=headers, files=files, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Attachment from Issue
def delete_attachment_from_issue(server_url: str, auth: Dict[str, str], attachment_id: str) -> str:
    """
    Deletes an attachment from an issue in a Jira project.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - attachment_id (str): The ID of the attachment to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/attachment/{attachment_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Attachment deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
