import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# Search Messages
def search_messages(token: str, query: str, count: int = 20, page: int = 1) -> Union[Dict[str, Any], str]:
    """
    Searches messages in a Slack workspace based on a query.

    Parameters:
    - token (str): The authentication token for Slack API.
    - query (str): The search query for messages.
    - count (int, optional): The number of results to return per page. Default is 20.
    - page (int, optional): The page number of the results to return. Default is 1.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/search.messages"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"query": query, "count": count, "page": page}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Search Files
def search_files(token: str, query: str, count: int = 20, page: int = 1) -> Union[Dict[str, Any], str]:
    """
    Searches files in a Slack workspace based on a query.

    Parameters:
    - token (str): The authentication token for Slack API.
    - query (str): The search query for files.
    - count (int, optional): The number of results to return per page. Default is 20.
    - page (int, optional): The page number of the results to return. Default is 1.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/search.files"
    headers = {"Authorization": f"Bearer {token}"}
    params = {"query": query, "count": count, "page": page}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
