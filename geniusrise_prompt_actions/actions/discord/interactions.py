import requests  # type: ignore
from typing import Union, Dict, Any, List
import logging


# Create Interaction
def create_interaction(
    token: str, application_id: str, name: str, description: str, options: List[Dict[str, Any]]
) -> Union[Dict[str, Any], str]:
    """
    Creates a new interaction (slash command) for a Discord application.

    Parameters:
    - token (str): The authentication token for Discord API.
    - application_id (str): The ID of the Discord application.
    - name (str): The name of the interaction.
    - description (str): The description of the interaction.
    - options (List[Dict[str, Any]]): A list of dictionaries containing options for the interaction. Optional.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/applications/{application_id}/commands"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"name": name, "description": description, "options": options}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Get Interaction Details
def get_interaction_details(token: str, application_id: str, interaction_id: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves the details of an interaction (slash command) for a Discord application.

    Parameters:
    - token (str): The authentication token for Discord API.
    - application_id (str): The ID of the Discord application.
    - interaction_id (str): The ID of the interaction to retrieve.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the interaction details or an error message.
    """
    url = f"https://discord.com/api/v9/applications/{application_id}/commands/{interaction_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Interaction
def update_interaction(
    token: str,
    application_id: str,
    interaction_id: str,
    name: str,
    description: str,
    options: List[Dict[str, Any]],
) -> Union[Dict[str, Any], str]:
    """
    Updates an existing interaction (slash command) for a Discord application.

    Parameters:
    - token (str): The authentication token for Discord API.
    - application_id (str): The ID of the Discord application.
    - interaction_id (str): The ID of the interaction to update.
    - name (str): The new name of the interaction.
    - description (str): The new description of the interaction.
    - options (List[Dict[str, Any]]): A list of dictionaries containing new options for the interaction. Optional.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the updated interaction details or an error message.
    """
    url = f"https://discord.com/api/v9/applications/{application_id}/commands/{interaction_id}"
    headers = {"Authorization": f"Bot {token}"}
    payload = {"name": name, "description": description, "options": options}

    try:
        response = requests.patch(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Interaction
def delete_interaction(token: str, application_id: str, interaction_id: str) -> Union[Dict[str, Any], str]:
    """
    Deletes an interaction (slash command) for a Discord application.

    Parameters:
    - token (str): The authentication token for Discord API.
    - application_id (str): The ID of the Discord application.
    - interaction_id (str): The ID of the interaction to delete.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from Discord API or an error message.
    """
    url = f"https://discord.com/api/v9/applications/{application_id}/commands/{interaction_id}"
    headers = {"Authorization": f"Bot {token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
