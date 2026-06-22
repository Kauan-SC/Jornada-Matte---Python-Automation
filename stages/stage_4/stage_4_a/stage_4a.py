from constants import RoleAssignees, TaskStatus, get_due_date
from core.logger import get_logger
from integrations.clickup import create_subtask, create_task

logger = get_logger(__name__)

def create_stage_4a(project: dict) -> str | None:

    logger.info(f"Etapa 4A Iniciada - {project['company_name']}")

    data = get_due_date(3)

    # Create Task - Fourth Step - CRM Onboarding
    task = create_task(
        name=f"Onboarding do CRM - {project['company_name']}",
        status=TaskStatus.REUNIOES_KAUAN,
        description=(
            "As próximas etapas são:\n\n"
            
            "- Marcar Onboarding do CRM com todo o time\n"
            "- Feedback do Onboarding do CRM\n"
            "- Pedir Indicação\n"),
        assignees=RoleAssignees.GESTOR,
        due_date=data
    )

    if task is None:
        logger.error(f"Erro na Etapa 4A - {project['company_name']}")
        return None
    
    task_id = task["id"]


    # Create Subtask - Third Step - A
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

    FEEDBACK_ONBOARDING = {
        "name": "Feedback do Onboarding do CRM",
        "description": (
            "Enviar mensagem no privado do cliente:\n\n"
            "Ola, tudo bem? Passando aqui para saber o que achou da reunião de Onboarding e como está sendo o projeto até agora. Tem algum elogio ou crítica?\n\n"
            "Sua opinião é muito importante pra gente e levamos isso muito a sério 🙏"
        ),
    }

    INDICACAO = {
        "name": "Pedir Indicação",
        "description": (
            "⚠️ Executar apenas se o cliente respondeu positivamente no Feedback do Onboarding.\n\n"
            "Enviar mensagem:\n\n"
            "Que legal! Ficamos muito felizes em saber que está gostando 😄\n\n"
            "Se você conhecer alguém que acha que esse sistema também pode fazer sentido para o negócio dela, e puder nos repassar o contato, ficaremos muito gratos!\n\n"
        ),
    }

    SUBTASKS = [MARCAR_ONBOARDING_CRM, FEEDBACK_ONBOARDING, INDICACAO]

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