import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# Add Reaction
def add_reaction(token: str, channel: str, name: str, timestamp: str) -> Union[Dict[str, Any], str]:
    """
    Adds a reaction to an item (message, file, etc.) in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel (str): The channel where the item is located.
    - name (str): The name of the reaction (emoji) to add.
    - timestamp (str): The timestamp of the message to react to.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reactions.add"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel, "name": name, "timestamp": timestamp}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Remove Reaction
def remove_reaction(token: str, channel: str, name: str, timestamp: str) -> Union[Dict[str, Any], str]:
    """
    Removes a reaction from an item (message, file, etc.) in a Slack channel.

    Parameters:
    - token (str): The authentication token for Slack API.
    - channel (str): The channel where the item is located.
    - name (str): The name of the reaction (emoji) to remove.
    - timestamp (str): The timestamp of the message to remove the reaction from.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reactions.remove"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"channel": channel, "name": name, "timestamp": timestamp}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Reactions
def list_reactions(token: str, user: str, full: bool = False) -> Union[Dict[str, Any], str]:
    """
    Lists all reactions for items (messages, files, etc.) that a user has reacted to.

    Parameters:
    - token (str): The authentication token for Slack API.
    - user (str, optional): The ID of the user to get reactions for. If not provided, the authenticated user is used.
    - full (bool, optional): Indicates whether to include full reaction details. Default is False.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reactions.list"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"user": user, "full": full}

    try:
        response = requests.get(url, headers=headers, params=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
