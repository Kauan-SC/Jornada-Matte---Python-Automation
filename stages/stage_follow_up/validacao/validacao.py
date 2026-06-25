from constants import TaskStatus
from core.logger import get_logger
from integrations.clickup import create_task

logger = get_logger(__name__)

# Create Validacao task
def validacao(project: dict) -> None:

    logger.info(f"Validação - {project['company_name']}")

    # Create Task - validação
    task = create_task(
        name=f"Validação semanal - {project['company_name']}",
        status=TaskStatus.PROJETO_FINALIZADO,
        description=(
        "- Mandar painel da IA e retorno do sistema para o Lead"),        
    )

    if task is None:
        logger.error(f"Erro na Etapa Validação - {project['company_name']}")
        return None
    
    logger.info(f"Etapa Validação iniciada - {project['company_name']}")
 