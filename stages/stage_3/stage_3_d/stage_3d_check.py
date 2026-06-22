from constants import Stages
from core.database import get_active_projects_by_stage, update_project
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_4.stage_4_b.stage_4b import create_stage_4b

logger = get_logger(__name__)

# Check if projects are completed using the ID to get the task infos
def check_stage_3d() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_3D)

    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 3D concluida. Criando Etapa 4B")

            new_task_id  = create_stage_4b(project)

            if new_task_id  is None:
                logger.error(f"Projeto {project['company_name']}: Falha ao criar Etapa 4B. Banco não atualizado.")
                continue

            update_project(project["id"], Stages.STAGE_4B, new_task_id )