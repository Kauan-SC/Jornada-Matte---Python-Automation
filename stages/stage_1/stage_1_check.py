from constants import Stages
from core.database import get_active_projects_by_stage, update_project
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_2.stage_2 import create_stage_2

logger = get_logger(__name__)

# ETAPA: 1 Check - Verifica se a Etapa 1 foi concluída e cria a Etapa 2

def check_stage_1() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_1)    # Obter todos os projetos ativos na Etapa 1

    # Para cada projeto, verificar se a tarefa da Etapa 1 foi concluída
    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 1 concluida. Criando Etapa 2")
            new_task_id = create_stage_2(project)

            # Se a criação da Etapa 2 falhar, logar o erro e continuar com o próximo projeto
            if new_task_id is None:
                logger.error(f"Projeto {project['company_name']}: Deu falha ao criar etapa 2. Banco não atualizado")
                continue

            update_project(project["id"], Stages.STAGE_2, new_task_id)
