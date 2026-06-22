from constants import RoleAssignees, TaskStatus, get_due_date
from core.logger import get_logger
from integrations.clickup import create_task

logger = get_logger(__name__)

def create_stage_3d(project: dict) -> str | None:

    logger.info(f"Etapa 3D Iniciada - {project['company_name']}")

    data = get_due_date(3)

    # Create Task - Third Step - D
    task = create_task(
        name=f"Realizar entrega da IA - {project['company_name']}",
        status=TaskStatus.TAREFAS_CS,
        description=(
        "Conectar a IA e realizar a entrega para testes do cliente:\n"),
        assignees=RoleAssignees.CS,
        due_date=data
    )

    if task is None:
        logger.error(f"Erro na Etapa 3D - {project['company_name']}")
        return None
    
    task_id = task["id"]
    logger.info(f"Etapa 3D iniciada - {project['company_name']} - Task-Id: {task_id}")
    return task_id
