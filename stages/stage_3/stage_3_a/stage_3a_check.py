from constants import Stages
from core.database import get_active_projects_by_stage, update_project
from core.logger import get_logger
from integrations.clickup import is_task_completed
from stages.stage_4.stage_4a import create_stage_4a

logger = get_logger(__name__)

# ETAPA: 3A Check - Verifica se a Etapa 3A foi concluída e cria a Etapa 4A

def check_stage_3a() -> None:
    projects = get_active_projects_by_stage(Stages.STAGE_3A)    # Obter todos os projetos ativos na Etapa 3A

    # Para cada projeto, verificar se a tarefa da Etapa 3A foi concluída
    for project in projects:
        if is_task_completed(project["task_id"]):
            logger.info(f"Projeto {project['company_name']}: Etapa 3A concluida. Criando Etapa 4A")

            new_task_id  = create_stage_4a(project)    # Criar a Etapa 4A

            # Se a criação da Etapa 3A falhar, logar o erro e continuar com o próximo projeto
            if new_task_id  is None:
                logger.error(f"Projeto {project['company_name']}: Falha ao criar Etapa 4A. Banco não atualizado.")
                continue

            update_project(project["id"], Stages.STAGE_4A, new_task_id )