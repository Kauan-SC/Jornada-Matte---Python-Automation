import random

from constants import RoleAssignees, TaskStatus, get_due_date
from core.logger import get_logger
from integrations.clickup import create_task, get_task

logger = get_logger(__name__)

def get_reviewer_dev(task_id_3b: str) -> list[int]:
    task = get_task(task_id_3b)
    if task is None:
        return [random.choice(RoleAssignees.DEVS)]
    
    assignee_ids = {a["id"]for a in task.get("assignees", [])}
    other_devs = [dev for dev in RoleAssignees.DEVS if dev not in assignee_ids]

    return [random.choice(other_devs)] if other_devs else [random.choice(RoleAssignees.DEVS)]

# Create Task - Third Step - Verification of AI
def create_stage_3c(project: dict) -> str | None:
    logger.info(f"Etapa 3C Iniciada - {project['company_name']}")

    data = get_due_date(5)
    reviewer = get_reviewer_dev(project["task_id"])

    task = create_task(
        name=f"Revisão da IA - {project['company_name']}",
        status=TaskStatus.TAREFAS_DEV,
        description=(
        "Necessário realizar a revisão da IA, o que verificar:\n\n"
        
        "- Prompt conciso e fazendo sentido\n"
        "- Fluxos de trabalho sendo acionados\n"
        "- Campos Personalizados sendo preenchidos\n"
        "- IA respondendo de forma coerente e sem alucinações\n"
        "- IA realizando agendamento OU repassando para consultor\n"),
        assignees=reviewer,
        due_date=data
    )

    if task is None:
        logger.error(f"Erro na Etapa 3C - {project['company_name']}")
        return None
    
    task_id = task["id"]
    logger.info(f"Etapa 3C iniciada - {project['company_name']} - Task-Id: {task_id}")
    return task_id