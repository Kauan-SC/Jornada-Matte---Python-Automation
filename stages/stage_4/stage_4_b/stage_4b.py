from constants import RoleAssignees, TaskStatus
from core.logger import get_logger
from integrations.clickup import create_subtask, create_task

logger = get_logger(__name__)

def create_stage_4b(project: dict) -> str | None:

    logger.info(f"Etapa 4B Iniciada - {project['company_name']}")


    # Create Task - Fourth Step - CRM Onboarding
    task = create_task(
        name=f"Plano de Ação de 90 Dias - {project['company_name']}",
        status=TaskStatus.REUNIOES_PEDRO,
        description=(
            "As próximas etapas são:\n\n"
            
            "- Marcar Reunião de Plano de Ação de 90 Dias\n"
            "- Feedback Pós-Reunião de 90 Dias\n"),
        assignees=RoleAssignees.CS,
    )

    if task is None:
        logger.error(f"Erro na Etapa 4B - {project['company_name']}")
        return None
    
    task_id = task["id"]


    # Create Subtask - Third Step - A
    MARCAR_PLANO_DE_ACAO = {
        "name": f"Marcar Reunião de Plano de Ação de 90 Dias - {project['company_name']}",
        "description": (
            f"Marcar Reunião de Plano de Ação de 90 Dias - {project['company_name']}\n\n\n"

            "Enviar mensagem:\n\n"

            "Pessoal, agora que realizamos a primeira entrega da IA, podemos marcar a reunião de Plano de Ação de 90 Dias!\n\n"
            "Será um encontro direto com o Pedro, nosso founder, focado exclusivamente na estratégia para escalar ainda mais a empresa de vocês usando Inteligência Artificial.\n\n"
            "Como está a agenda de vocês? 🚀"
        ),
    }

    FEEDBACK_PLANO_DE_ACAO = {
        "name": "Feedback da Reunião de Plano de Ação de 90 Dias",
        "description": (
            "Enviar mensagem no privado do cliente:\n\n"
            "Ola, tudo bem? Passando aqui para saber o que achou da reunião de Plano de Ação com o Pedro e como está sendo o projeto até agora. Tem algum elogio ou crítica?\n\n"
            "Sua opinião é muito importante pra gente e levamos isso muito a sério 🙏"
        ),
    }

    SUBTASKS = [MARCAR_PLANO_DE_ACAO, FEEDBACK_PLANO_DE_ACAO]

    for subtask in SUBTASKS:
        create_subtask(
            parent_task_id=task_id,
            name=subtask["name"],
            description=subtask.get("description", ""),
            assignees=RoleAssignees.CS,
        )
       
    logger.info(f"Etapa 4B iniciada - {project['company_name']} - Task-Id: {task_id}")
    return task_id