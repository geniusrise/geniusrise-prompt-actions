import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Create Space
def create_space(base_url: str, auth: tuple, space_key: str, name: str, description: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new space in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - space_key (str): The key for the new space.
    - name (str): The name of the new space.
    - description (str): The description of the new space.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/space"
    headers = {"Content-Type": "application/json"}
    payload = {
        "key": space_key,
        "name": name,
        "description": {"plain": {"value": description, "representation": "plain"}},
    }

    try:
        response = requests.post(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Space
def read_space(base_url: str, auth: tuple, space_key: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a Confluence space by its key.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - space_key (str): The key of the space to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/space/{space_key}"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Space
def update_space(base_url: str, auth: tuple, space_key: str, name: str, description: str) -> Union[Dict[str, Any], str]:
    """
    Updates an existing Confluence space.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - space_key (str): The key of the space to update.
    - name (str): The new name for the space.
    - description (str): The new description for the space.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/space/{space_key}"
    headers = {"Content-Type": "application/json"}
    payload = {"name": name, "description": {"plain": {"value": description, "representation": "plain"}}}

    try:
        response = requests.put(url, headers=headers, json=payload, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Space
def delete_space(base_url: str, auth: tuple, space_key: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a Confluence space by its key.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - space_key (str): The key of the space to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/space/{space_key}"

    try:
        response = requests.delete(url, auth=auth)
        response.raise_for_status()
        return {"status": "Space deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Spaces
def list_all_spaces(base_url: str, auth: tuple, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Lists all spaces in a Confluence instance.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - limit (int, optional): The maximum number of spaces to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/space"
    params = {"limit": limit}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
