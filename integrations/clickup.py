import requests

from config import CLICKUP_API_KEY, CLICKUP_LIST_ID
from core.logger import get_logger

logger = get_logger(__name__)

BASE_URL = "https://api.clickup.com/api/v2"
HEADERS = {
    "Authorization": CLICKUP_API_KEY,
    "Content-Type": "application/json"
}

# Create Task - Object
def create_task(name: str, description: str = "", markdown_content: str = "", assignees: list | None = None, due_date: str | None = None, status: str | None = None) -> dict | None:
    url = f"{BASE_URL}/list/{CLICKUP_LIST_ID}/task"
    payload = {
        "name": name,
        "description": description,
        "markdown_content": markdown_content,
        "assignees": assignees or [],
        "due_date": due_date
    }
    if status:
        payload["status"] = status
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        task = response.json()
        logger.info(f"Tarefa criada: {task['name']}  ID: {task['id']}")
        return task
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao criar tarefa: '{name}': {e}")
        return None

# --------------------------------------------------------------------------------------------------------------------------------------------

# Create Sub-Task - Object
def create_subtask(parent_task_id: str, name: str, description: str = "", markdown_content: str = "", assignees: list = [], due_date: str | None = None) -> dict | None:
    url = f"{BASE_URL}/list/{CLICKUP_LIST_ID}/task"
    payload = {
        "name": name,
        "description": description,
        "markdown_content": markdown_content,
        "assignees": assignees,
        "due_date": due_date,
        "parent": parent_task_id
    }
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()
        subtask = response.json()
        logger.info(f"Sub-tarefa criada: {subtask['name']}  ID: {subtask['id']}")
        return subtask
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao criar tarefa: '{name}': {e}")
        return None
    
# --------------------------------------------------------------------------------------------------------------------------------------------

# Get task_id - Object (Get Id Tasks for Sub-Task Creation)
def get_task(task_id: str) -> dict | None:
    url = f"{BASE_URL}/task/{task_id}"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        get_task = response.json()
        logger.info(f"Tarefa obtida: {get_task['name']}  ID: {get_task['id']}")
        return get_task
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao obter tarefa ID: '{task_id}': {e}")
        return None
    
# --------------------------------------------------------------------------------------------------------------------------------------------

# Get tasks - Object (Get the "Open Tasks" for Dashboard)
def get_tasks(statuses: list | None = None, assignees: list | None = None) -> list | None:
    url = f"{BASE_URL}/list/{CLICKUP_LIST_ID}/task"
    params = {}
    if statuses:
        params["statuses[]"] = statuses
    if assignees:
        params["assignees[]"] = assignees
    try:
        response = requests.get(url, params=params, headers=HEADERS)
        response.raise_for_status()
        tasks = response.json().get("tasks", [])
        logger.info(f"{len(tasks)} tarefas obtidas da List ID: '{CLICKUP_LIST_ID}'")
        return tasks
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro ao obter tarefas da List ID: '{CLICKUP_LIST_ID}': {e}")
        return None   
    
# --------------------------------------------------------------------------------------------------------------------------------------------

# Task Status - Object
def is_task_completed(task_id: str) -> bool:
    task = get_task(task_id)
    if task is None:
        return False
    return task.get("status", {}).get("type", "") == "closed"
    