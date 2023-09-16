import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# Pin Item
def pin_item(token: str, channel: str, timestamp: str) -> Union[Dict[str, Any], str]:
    """
    Pins an item (message, file, etc.) in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel (str): The channel where the item is located.
    - timestamp (str): The timestamp of the message to pin.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/pins.add"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel, "timestamp": timestamp}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Unpin Item
def unpin_item(token: str, channel: str, timestamp: str) -> Union[Dict[str, Any], str]:
    """
    Unpins an item (message, file, etc.) in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel (str): The channel where the item is located.
    - timestamp (str): The timestamp of the message to unpin.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/pins.remove"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel, "timestamp": timestamp}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Pinned Items
def list_pinned_items(token: str, channel: str) -> Union[Dict[str, Any], str]:
    """
    Lists all pinned items in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel (str): The channel where the pinned items are located.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/pins.list"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel}

    try:
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
