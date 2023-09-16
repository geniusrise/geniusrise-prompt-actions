import requests  # type: ignore
from typing import Union, Dict, Any
import logging


# Search Content
def search_content(base_url: str, auth: tuple, query: str, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Searches for content in Confluence based on a query.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - query (str): The search query.
    - limit (int, optional): The maximum number of search results to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/content/search"
    params = {"cql": query, "limit": limit}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Search Users
def search_users(base_url: str, auth: tuple, query: str, limit: int = 25) -> Union[Dict[str, Any], str]:
    """
    Searches for users in Confluence based on a query.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - query (str): The search query.
    - limit (int, optional): The maximum number of search results to return. Default is 25.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/user/search"
    params = {"query": query, "limit": limit}

    try:
        response = requests.get(url, params=params, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
