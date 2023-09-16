import logging
from typing import Dict, Any, Union

import requests  # type: ignore


# Create Worklog
def create_worklog(
    server_url: str,
    auth: Dict[str, str],
    issue_key: str,
    time_spent: str,
    start_date: str,
    adjust_for_daylight_saving: bool = True,
) -> Union[Dict[str, Any], str]:
    """
    Creates a new worklog for an issue.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - issue_key (str): The key of the issue the worklog is for.
    - time_spent (str): The time spent on the worklog, e.g. "3h".
    - start_date (str): The start date of the worklog, e.g. "2023-02-14".
    - adjust_for_daylight_saving (bool, optional): Whether to adjust the start date for daylight saving time. Defaults to True.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/issue/{issue_key}/worklog"
    headers = {"Content-Type": "application/json"}
    payload = {
        "timeSpent": time_spent,
        "started": start_date,
        "adjustForDST": adjust_for_daylight_saving,
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Worklog
def read_worklog(server_url: str, auth: Dict[str, str], worklog_id: str) -> Union[Dict[str, Any], str]:
    """
    Reads a worklog by its ID.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - worklog_id (str): The ID of the worklog to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/worklog/{worklog_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Worklog
def update_worklog(
    server_url: str,
    auth: Dict[str, str],
    worklog_id: str,
    time_spent: str,
    start_date: str,
    adjust_for_daylight_saving: bool = True,
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing worklog.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - worklog_id (str): The ID of the worklog to update.
    - time_spent (str): The new time spent on the worklog, e.g. "3h".
    - start_date (str): The new start date of the worklog, e.g. "2023-02-14".
    - adjust_for_daylight_saving (bool, optional): Whether to adjust the start date for daylight saving time. Defaults to True.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/api/2/worklog/{worklog_id}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "timeSpent": time_spent,
        "started": start_date,
        "adjustForDST": adjust_for_daylight_saving,
    }

    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Worklog
def delete_worklog(server_url: str, auth: Dict[str, str], worklog_id: str) -> str:
    """
    Deletes a worklog by its ID.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - worklog_id (str): The ID of the worklog to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/api/2/worklog/{worklog_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Worklog deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
