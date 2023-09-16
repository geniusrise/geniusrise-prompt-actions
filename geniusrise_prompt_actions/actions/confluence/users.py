import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Get User Details
def get_user_details(base_url: str, auth: tuple, username: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of a specific user in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - username (str): The username of the user whose details are to be retrieved.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/user"
    params = {"username": username}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update User Details
def update_user_details(
    base_url: str, auth: tuple, username: str, update_data: Dict[str, Any]
) -> Union[Dict[str, Any], str]:
    """
    Updates the details of a specific user in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - username (str): The username of the user whose details are to be updated.
    - update_data (Dict[str, Any]): A dictionary containing the fields to be updated.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/user"
    params = {"username": username}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.put(url, params=params, headers=headers, json=update_data, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
