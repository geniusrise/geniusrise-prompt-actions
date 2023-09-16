import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Create Webhook
def create_webhook(base_url: str, auth: tuple, webhook_data: Dict[str, Any]) -> Union[Dict[str, Any], str]:
    """
    Creates a new webhook in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - webhook_data (Dict[str, Any]): A dictionary containing the webhook data.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/webhook"
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, headers=headers, json=webhook_data, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Webhook
def delete_webhook(base_url: str, auth: tuple, webhook_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a webhook in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.
    - webhook_id (str): The ID of the webhook to be deleted.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Confluence API or an error message.
    """
    url = f"{base_url}/rest/api/webhook/{webhook_id}"

    try:
        response = requests.delete(url, auth=auth)
        response.raise_for_status()
        return {"status": "Webhook deleted successfully"}
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List All Webhooks
def list_all_webhooks(base_url: str, auth: tuple) -> Union[List[Dict[str, Any]], str]:
    """
    Lists all webhooks in Confluence.

    Parameters:
    - base_url (str): The base URL of the Confluence instance.
    - auth (tuple): A tuple containing the username and API token for authentication.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the webhooks or an error message.
    """
    url = f"{base_url}/rest/api/webhook"

    try:
        response = requests.get(url, auth=auth)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
