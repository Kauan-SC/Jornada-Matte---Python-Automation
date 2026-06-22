from constants import Stages
from core.database import get_active_projects_by_stage, update_project
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_final.stage_final import create_final_stage

logger = get_logger(__name__)

# Check if projects are completed using the ID to get the task infos
def check_stage_4a() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_4A)

    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 4A concluida. Personalização do CRM concluida!")

            update_project(project["id"], Stages.FINAL_STAGE, project["task_id"])


def check_stage_4b() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_4B)

    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 4B concluida. Criação da IA finalizada!")
            new_task_id = create_final_stage(project)

            if new_task_id is None:
                logger.error(f"Projeto {project['company_name']}: Deu falha ao criar etapa final. Banco não atualizado")
                continue

            update_project(project["id"], Stages.FINAL_STAGE, new_task_id)
