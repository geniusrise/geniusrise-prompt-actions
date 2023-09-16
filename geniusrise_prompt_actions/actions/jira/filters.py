import logging
from typing import Dict, List, Any, Union

import requests  # type: ignore


# Create Filter
def create_filter(
    server_url: str, auth: Dict[str, str], name: str, jql: str, description: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new filter in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - name (str): The name of the new filter.
    - jql (str): The JQL query for the filter.
    - description (str): The description of the filter.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/filter"
    headers = {"Content-Type": "application/json"}
    payload = {"name": name, "jql": jql, "description": description}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Filter
def read_filter(server_url: str, auth: Dict[str, str], filter_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a filter from Jira by its ID.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - filter_id (int): The ID of the filter to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/filter/{filter_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Filter
def update_filter(
    server_url: str, auth: Dict[str, str], filter_id: int, new_name: str, new_jql: str, new_description: str
) -> Union[Dict[str, Any], str]:
    """
    Updates a filter's details in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - filter_id (int): The ID of the filter to update.
    - new_name (str): The new name for the filter.
    - new_jql (str): The new JQL query for the filter.
    - new_description (str): The new description for the filter.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/filter/{filter_id}"
    headers = {"Content-Type": "application/json"}
    payload = {"name": new_name, "jql": new_jql, "description": new_description}

    try:
        response = requests.put(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Filter
def delete_filter(server_url: str, auth: Dict[str, str], filter_id: int) -> str:
    """
    Deletes a filter from Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - filter_id (int): The ID of the filter to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/filter/{filter_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Filter deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Filters
def list_all_filters(server_url: str, auth: Dict[str, str]) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all filters in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the filters or an error message.
    """
    url = f"{server_url}/rest/api/2/filter"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json().get("values", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
