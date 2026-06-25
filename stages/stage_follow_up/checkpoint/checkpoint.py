from constants import TaskStatus
from core.logger import get_logger
from integrations.clickup import create_task

logger = get_logger(__name__)

# Create checkpoint task
def checkpoint(project: dict) -> None:

    logger.info(f"Checkpoint - {project['company_name']}")

    # Create Task - Checkpoint
    task = create_task(
        name=f"Checkpoint - Reunião Mensal - {project['company_name']}",
        status=TaskStatus.PROJETO_FINALIZADO,
        description=(
        "- Realizar reunião mensal com cliente, buscando Feedback e indicações"),
    )

    if task is None:
        logger.error(f"Erro na Etapa Checkpoint - {project['company_name']}")
        return None
    
    logger.info(f"Etapa Checkpoint iniciada - {project['company_name']}")
    

