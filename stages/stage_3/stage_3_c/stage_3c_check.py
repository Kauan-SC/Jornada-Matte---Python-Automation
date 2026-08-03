from constants import Stages
from core.database import get_active_projects_by_stage, update_project
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_3.stage_3_d.stage_3d import create_stage_3d

logger = get_logger(__name__)

# ETAPA: 3C - Revisão da IA

def check_stage_3c() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_3C)    # Obter todos os projetos ativos na Etapa 3C

    # Para cada projeto, verificar se a tarefa da Etapa 3C foi concluída
    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 3C concluida. Criando Etapa 3D")

            new_task_id  = create_stage_3d(project)    # Criar a Etapa 3D

            # Se a criação da Etapa 3D falhar, logar o erro e continuar com o próximo projeto
            if new_task_id  is None:
                logger.error(f"Projeto {project['company_name']}: Falha ao criar Etapa 3D. Banco não atualizado.")
                continue

            update_project(project["id"], Stages.STAGE_3D, new_task_id )
