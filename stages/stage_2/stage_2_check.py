from constants import Stages
from core.database import (
    get_active_projects_by_stage,
    insert_project_branch,
    update_project,
)
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_3.stage_3_a.stage_3a import create_stage_3a
from stages.stage_3.stage_3_b.stage_3b import create_stage_3b

logger = get_logger(__name__)

# Check if projects are completed using the ID to get the task infos
def check_stage_2() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_2)

    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 2 concluida. Criando Etapa 3 A e B")

            new_task_id_a = create_stage_3a(project)
            new_task_id_b = create_stage_3b(project)

            if new_task_id_a is None:
                logger.error(f"Projeto {project['company_name']}: Falha ao criar Etapa 3A. Banco não atualizado.")
                continue

            if new_task_id_b is None:
                logger.error(f"Projeto {project['company_name']}: Falha ao criar Etapa 3B. Banco não atualizado.")
                continue

            update_project(project["id"], Stages.STAGE_3A, new_task_id_a)
            insert_project_branch(project, Stages.STAGE_3B, new_task_id_b)