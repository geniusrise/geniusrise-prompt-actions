import logging
from typing import Dict, List, Any, Union

import requests  # type: ignore


# Create Sprint
def create_sprint(
    server_url: str, auth: Dict[str, str], board_id: int, sprint_name: str, start_date: str, end_date: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new sprint in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - board_id (int): The ID of the board where the sprint will be created.
    - sprint_name (str): The name of the new sprint.
    - start_date (str): The start date of the sprint (format: "yyyy-mm-dd").
    - end_date (str): The end date of the sprint (format: "yyyy-mm-dd").

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/board/{board_id}/sprint"
    headers = {"Content-Type": "application/json"}
    payload = {"name": sprint_name, "startDate": start_date, "endDate": end_date}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Sprint
def read_sprint(server_url: str, auth: Dict[str, str], sprint_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a sprint from Jira by its ID.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - sprint_id (int): The ID of the sprint to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/sprint/{sprint_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Sprint
def update_sprint(
    server_url: str, auth: Dict[str, str], sprint_id: int, new_name: str, new_start_date: str, new_end_date: str
) -> Union[Dict[str, Any], str]:
    """
    Updates a sprint's details in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - sprint_id (int): The ID of the sprint to update.
    - new_name (str): The new name for the sprint.
    - new_start_date (str): The new start date for the sprint (format: "yyyy-mm-dd").
    - new_end_date (str): The new end date for the sprint (format: "yyyy-mm-dd").

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/sprint/{sprint_id}"
    headers = {"Content-Type": "application/json"}
    payload = {"name": new_name, "startDate": new_start_date, "endDate": new_end_date}

    try:
        response = requests.put(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Sprint
def delete_sprint(server_url: str, auth: Dict[str, str], sprint_id: int) -> str:
    """
    Deletes a sprint from Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - sprint_id (int): The ID of the sprint to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/sprint/{sprint_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Sprint deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Sprints
def list_all_sprints(server_url: str, auth: Dict[str, str], board_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all sprints in a Jira board.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - board_id (int): The ID of the board to list sprints from.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the sprints or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/board/{board_id}/sprint"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json().get("values", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
