import logging
from typing import Any, Dict, List, Union

import requests  # type: ignore


# Create Pipeline
def create_pipeline(server_url: str, auth_token: str, project_id: int, ref: str) -> Union[Dict[str, Any], str]:
    """
    Creates a new pipeline in a GitLab project.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the pipeline will be created.
    - ref (str): The branch or tag name for which to run the pipeline.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/pipeline"
    headers = {"Authorization": f"Bearer {auth_token}"}
    payload = {"ref": ref}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Read Pipeline
def read_pipeline(server_url: str, auth_token: str, project_id: int, pipeline_id: int) -> Union[Dict[str, Any], str]:
    """
    Retrieves details of a GitLab pipeline by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the pipeline resides.
    - pipeline_id (int): The ID of the pipeline to read.

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/pipelines/{pipeline_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Update Pipeline
def update_pipeline(
    server_url: str, auth_token: str, project_id: int, pipeline_id: int, action: str
) -> Union[Dict[str, Any], str]:
    """
    Updates a GitLab pipeline by its ID and project ID. Currently, only action 'cancel' is supported.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the pipeline resides.
    - pipeline_id (int): The ID of the pipeline to update.
    - action (str): The action to perform on the pipeline ('cancel').

    Returns:
    - Union[Dict[str, Any], str]: A dictionary containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/pipelines/{pipeline_id}/{action}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Delete Pipeline
def delete_pipeline(server_url: str, auth_token: str, project_id: int, pipeline_id: int) -> str:
    """
    Deletes a GitLab pipeline by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the pipeline resides.
    - pipeline_id (int): The ID of the pipeline to delete.

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/pipelines/{pipeline_id}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return "Pipeline deleted successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Pipeline Jobs
def list_pipeline_jobs(
    server_url: str, auth_token: str, project_id: int, pipeline_id: int
) -> Union[List[Dict[str, Any]], str]:
    """
    Lists jobs of a GitLab pipeline by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the pipeline resides.
    - pipeline_id (int): The ID of the pipeline whose jobs to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/pipelines/{pipeline_id}/jobs"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# List Pipeline Schedules
def list_pipeline_schedules(server_url: str, auth_token: str, project_id: int) -> Union[List[Dict[str, Any]], str]:
    """
    Lists pipeline schedules of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose pipeline schedules to list.

    Returns:
    - Union[List[Dict[str, Any]], str]: A list of dictionaries containing the response from GitLab API or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/pipeline_schedules"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Pipeline Jobs
def manage_pipeline_jobs(server_url: str, auth_token: str, project_id: int, job_id: int, action: str) -> str:
    """
    Manages jobs of a GitLab pipeline by its ID and project ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project where the pipeline resides.
    - job_id (int): The ID of the job to manage.
    - action (str): The action to perform on the job ('cancel', 'retry').

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/jobs/{job_id}/{action}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return f"Job {action}ed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)


# Manage Pipeline Schedules
def manage_pipeline_schedules(server_url: str, auth_token: str, project_id: int, schedule_id: int, action: str) -> str:
    """
    Manages pipeline schedules of a GitLab project by its ID.

    Parameters:
    - server_url (str): The URL of the GitLab server.
    - auth_token (str): The authentication token for GitLab API.
    - project_id (int): The ID of the project whose pipeline schedules to manage.
    - schedule_id (int): The ID of the schedule to manage.
    - action (str): The action to perform on the schedule ('take_ownership', 'play').

    Returns:
    - str: A success message or an error message.
    """
    url = f"{server_url}/api/v4/projects/{project_id}/pipeline_schedules/{schedule_id}/{action}"
    headers = {"Authorization": f"Bearer {auth_token}"}

    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        return f"Schedule {action}ed successfully."
    except requests.RequestException as e:
        logging.error(f"An error occurred: {e}")
        return str(e)
