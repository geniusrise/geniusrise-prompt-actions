import logging
from typing import Any, Dict, Union

import requests  # type: ignore


# Create Wiki Page
def create_wiki_page(
    server_url: str, auth_token: str, project_id: int, title: str, content: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new wiki page in a GitLab project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the wiki page will be created.
    - title (str): The title of the wiki page.
    - content (str): The content of the wiki page.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/wikis"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"title": title, "content": content}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Wiki Page
def read_wiki_page(server_url: str, auth_token: str, project_id: int, slug: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves a wiki page in a GitLab project by its slug.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the wiki page resides.
    - slug (str): The slug (URL path) of the wiki page to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/wikis/{slug}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Wiki Page
def update_wiki_page(
    server_url: str,
    auth_token: str,
    project_id: int,
    slug: str,
    title: str,
    content: str,
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing wiki page in a GitLab project by its slug.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the wiki page resides.
    - slug (str): The slug (URL path) of the wiki page to update.
    - title (str): The new title of the wiki page.
    - content (str): The new content of the wiki page.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/wikis/{slug}"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"title": title, "content": content}

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Wiki Page
def delete_wiki_page(server_url: str, auth_token: str, project_id: int, slug: str) -> str:
    """
    Deletes a wiki page in a GitLab project by its slug.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the wiki page resides.
    - slug (str): The slug (URL path) of the wiki page to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/wikis/{slug}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Wiki page deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
