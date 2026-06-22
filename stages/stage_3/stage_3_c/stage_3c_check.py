from constants import Stages
from core.database import get_active_projects_by_stage, update_project
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_3.stage_3_d.stage_3d import create_stage_3d

logger = get_logger(__name__)

# Check if projects are completed using the ID to get the task infos
def check_stage_3c() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_3C)

    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 3C concluida. Criando Etapa 3D")

            new_task_id  = create_stage_3d(project)

            if new_task_id  is None:
                logger.error(f"Projeto {project['company_name']}: Falha ao criar Etapa 3D. Banco não atualizado.")
                continue

            update_project(project["id"], Stages.STAGE_3D, new_task_id )
