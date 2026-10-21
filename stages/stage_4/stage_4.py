from constants import RoleAssignees, TaskStatus, get_due_date
from core.logger import get_logger
from integrations.clickup import create_subtask, create_task

logger = get_logger(__name__)

# ETAPA: 4A - Onboarding do CRM

def create_stage_4a(project: dict) -> str | None:

    # Histórico do projeto no log
    logger.info(f"Etapa 4A Iniciada - {project['company_name']}")

    # Data de vencimento da tarefa, 3 dias a partir da criação
    data = get_due_date(3)

    # Criar a tarefa principal no ClickUp
    task = create_task(
        name=f"Onboarding do CRM - {project['company_name']}",
        status=TaskStatus.REUNIOES_KAUAN,
        description=(
            "- Marcar Onboarding do CRM com todo o time\n"),
        assignees=RoleAssignees.GESTOR,
        due_date=data
    )

    # Se a tarefa não for criada, logar o erro e retornar None
    if task is None:
        logger.error(f"Erro na Etapa 4A - {project['company_name']}")
        return None
    
    task_id = task["id"]

# ----------------------------------------------------------------------------------------------------------------------------------------------

    # Dados de cada subtarefa
    MARCAR_ONBOARDING_CRM = {
        "name": f"Onboarding do CRM - {project['company_name']}",
        "description": (
            f"Marcar o Onboarding do CRM - {project['company_name']}\n\n\n"

            "Enviar mensagem:\n\n"
            
            "Boa tarde pessoal!\n"
            "Agora que o CRM já foi todo personalizado, podemos marcar a reunião de Onboarding para mostrar todas as funcionalidades e opções possíveis ali dentro\n"
            "Como está a disponibilidade de vocês?"
        ),
    }

    SUBTASKS = [MARCAR_ONBOARDING_CRM]

# ----------------------------------------------------------------------------------------------------------------------------------------------

    # Criar as subtarefas no ClickUp
    for subtask in SUBTASKS:
        create_subtask(
            parent_task_id=task_id,
            name=subtask["name"],
            description=subtask.get("description", ""),
            assignees=RoleAssignees.GESTOR,
            due_date=data
        )
       
    logger.info(f"Etapa 4A iniciada - {project['company_name']} - Task-Id: {task_id}")
    return task_id