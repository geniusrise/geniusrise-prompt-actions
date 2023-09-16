import logging
from typing import Dict, List, Any, Union

import requests  # type: ignore


# Create Board
def create_board(
    server_url: str, auth: Dict[str, str], board_name: str, board_type: str, project_key: str
) -> Union[Dict[str, Any], str]:
    """
    Creates a new board in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - board_name (str): The name of the new board.
    - board_type (str): The type of the board ('scrum' or 'kanban').
    - project_key (str): The project key where the board will be created.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/board"
    headers = {"Content-Type": "application/json"}
    payload = {"name": board_name, "type": board_type, "location": {"projectKey": project_key}}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Board
def read_board(server_url: str, auth: Dict[str, str], board_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a board from Jira by its ID.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - board_id (int): The ID of the board to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/board/{board_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Board
def update_board(
    server_url: str, auth: Dict[str, str], board_id: int, new_name: str, new_type: str
) -> Union[Dict[str, Any], str]:
    """
    Updates a board's details in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - board_id (int): The ID of the board to update.
    - new_name (str): The new name for the board.
    - new_type (str): The new type for the board ('scrum' or 'kanban').

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    # Note: Jira API may not support board updates directly. This is a placeholder.
    # You may need to delete and recreate the board or use other methods to achieve this.
    logging.warning("Jira API may not support direct board updates. This is a placeholder function.")
    return "Board update feature may not be supported by Jira API."


# Delete Board
def delete_board(server_url: str, auth: Dict[str, str], board_id: int) -> str:
    """
    Deletes a board from Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - board_id (int): The ID of the board to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/board/{board_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Board deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Boards
def list_all_boards(server_url: str, auth: Dict[str, str]) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all boards in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the boards or an error message.
    """
    url = f"{server_url}/rest/agile/1.0/board"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json().get("values", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
