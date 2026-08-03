from constants import Stages
from core.database import get_active_projects_by_stage, update_completed_project
from core.logger import get_logger
from integrations.clickup import is_task_completed

logger = get_logger(__name__)

# ETAPA: 3D Check - Verifica se a Etapa 3D foi concluída e finaliza o projeto

def check_stage_3d() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_3D)    # Obter todos os projetos ativos na Etapa 3D

    # Para cada projeto, verificar se a tarefa da Etapa 2 foi concluída
    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 3D concluida. Criação da IA finalizada!")

            update_completed_project(project["id"], Stages.FINAL_STAGE_IA, project["task_id"])


