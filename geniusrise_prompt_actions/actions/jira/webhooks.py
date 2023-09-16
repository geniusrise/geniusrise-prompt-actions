import logging
from typing import Dict, List, Any, Union

import requests  # type: ignore


def create_webhook(
    server_url: str, auth: Dict[str, str], name: str, url: str, events: List[str]
) -> Union[Dict[str, Any], str]:
    """
    Creates a new webhook in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - name (str): The name of the new webhook.
    - url (str): The URL that this webhook will post data to.
    - events (List[str]): List of events for which this webhook will be triggered.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/webhooks/1.0/webhook"
    headers = {"Content-Type": "application/json"}
    payload = {"name": name, "url": url, "events": events}

    try:
        response = requests.post(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Webhook
def read_webhook(server_url: str, auth: Dict[str, str], webhook_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves a webhook from Jira by its ID.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - webhook_id (int): The ID of the webhook to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/webhooks/1.0/webhook/{webhook_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Webhook
def update_webhook(
    server_url: str, auth: Dict[str, str], webhook_id: int, new_name: str, new_url: str, new_events: List[str]
) -> Union[Dict[str, Any], str]:
    """
    Updates a webhook's details in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - webhook_id (int): The ID of the webhook to update.
    - new_name (str): The new name for the webhook.
    - new_url (str): The new URL that this webhook will post data to.
    - new_events (List[str]): List of new events for which this webhook will be triggered.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Jira API or an error message.
    """
    url = f"{server_url}/rest/webhooks/1.0/webhook/{webhook_id}"
    headers = {"Content-Type": "application/json"}
    payload = {"name": new_name, "url": new_url, "events": new_events}

    try:
        response = requests.put(url, headers=headers, json=payload, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Webhook
def delete_webhook(server_url: str, auth: Dict[str, str], webhook_id: int) -> str:
    """
    Deletes a webhook from Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.
    - webhook_id (int): The ID of the webhook to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/rest/webhooks/1.0/webhook/{webhook_id}"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.delete(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return "Webhook deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Webhooks
def list_all_webhooks(server_url: str, auth: Dict[str, str]) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all webhooks in Jira.

    Parameters:
    - server_url (str): The URL of the Jira server.
    - auth (Dict[str, str]): Dictionary containing 'username' and 'password' for basic authentication.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the webhooks or an error message.
    """
    url = f"{server_url}/rest/webhooks/1.0/webhook"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.get(url, headers=headers, auth=(auth["username"], auth["password"]))
        response.raise_for_status()
        return response.json().get("values", [])
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
