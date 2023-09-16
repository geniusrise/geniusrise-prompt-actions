import requests  # type: ignore
import logging
from typing import Union, Dict, Any


# Create Reminder
def create_reminder(token: str, text: str, time: str, user_id: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new reminder in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - text (str): The text of the reminder.
    - time (str): When the reminder will trigger (can be a formatted date/time string or delay string like "in 20 minutes").
    - user_id (str, optional): The ID of the user to whom the reminder is for. If not provided, the reminder is for the authenticated user.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reminders.add"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"text": text, "time": time, "user": user_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Reminder
def delete_reminder(token: str, reminder_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes a reminder in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.
    - reminder_id (str): The ID of the reminder to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reminders.delete"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"reminder": reminder_id}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Reminders
def list_reminders(token: str) -> Union[Dict[str, Any], str]:
    """
    Lists all reminders in a Slack workspace.

    Parameters:
    - token (str): The authentication token for Slack API.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Slack API or an error message.
    """
    url = "https://slack.com/api/reminders.list"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
