from constants import Stages
from core.database import get_active_projects_by_stage, update_project
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_2.stage_2 import create_stage_2

logger = get_logger(__name__)

# Check if projects are completed using the ID to get the task infos
def check_stage_1() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_1)

    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 1 concluida. Criando Etapa 2")
            new_task_id = create_stage_2(project)

            if new_task_id is None:
                logger.error(f"Projeto {project['company_name']}: Deu falha ao criar etapa 2. Banco não atualizado")
                continue

            update_project(project["id"], Stages.STAGE_2, new_task_id)
