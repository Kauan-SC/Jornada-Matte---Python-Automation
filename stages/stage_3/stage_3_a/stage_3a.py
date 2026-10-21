from constants import RoleAssignees, TaskStatus, get_due_date
from core.logger import get_logger
from integrations.clickup import create_subtask, create_task

logger = get_logger(__name__)

# ETAPA: 3A - Personalização do CRM, Cadastro de Leads, Calendários e Horários, Captação e Integração de Leads, Automações, Comunicação e Canais


def create_stage_3a(project: dict) -> str | None:

    # Histórico do projeto no log
    logger.info(f"Etapa 3A Iniciada - {project['company_name']}")

    # Data de vencimento da tarefa, 10 dias a partir da criação
    data = get_due_date(10)

    # Criar a tarefa principal no ClickUp
    task = create_task(
        name=f"Personalização do CRM - {project['company_name']}",
        status=TaskStatus.PERSONALIZAR_CRM,
        description=(
            f"Etapa de personalização do CRM de {project['company_name']}\n\n\n"

            f"Os próximos passos são divididos em etapas:\n\n"

            f"Cadastro de Leads, Calendários e Horários:\n"
            f"- Importação, tagueamento e personalização de Leads\n"
            f"- Importação, tagueamento e personalização de Pipeline\n"
            f"- Cadastro e ajuste de calendário por funcionário\n"
            f"- Ajuste de disponibilidade\n\n"

            f"Captação e Integração de Leads:\n"
            f"- Cadastro da Meta Ads (Facebook/Instagram)\n"
            f"- Criação de dashboard de leads da META\n"
            f"- Criação ou integração de formulários/sites\n\n"

            f"Automações:\n"
            f"- Divisão de Contatos\n"
            f"- Automação de respostas para posts no Instagram/Facebook/TikTok\n"
            
            f"Comunicação e Canais:\n"
            f"- Cadastro do WhatsApp Business\n"
            f"- Cadastro do WhatsApp API Oficial\n"
            f"- Cadastro de e-mail marketing\n\n"),
        assignees=RoleAssignees.GESTOR,
        due_date=data
    )

    # Se a tarefa não for criada, logar o erro e retornar None
    if task is None:
        logger.error(f"Erro na Etapa 3A - {project['company_name']}")
        return None
    
    task_id = task["id"]

# ----------------------------------------------------------------------------------------------------------------------------------------------

    # Dados de cada subtarefa
    SUBTASK_UNICA = {
        "name": "Personalização do CRM — Leads, Integrações e WhatsApp",
        "description": (
            "Boa tarde, @cliente!\n\n"

            "Para finalizar a personalização do CRM, precisamos de 4 informações/ações:\n\n"

            "1️⃣ E-mail do time:\n"
            "Para cadastrarmos os membros do time no sistema, envie Nome, Sobrenome, Telefone e E-mail de cada pessoa.\n\n"

            "2️⃣ Conectar Facebook/Instagram:\n"

            "3️⃣ Importar Leads\n"

            "4️⃣ Conectar WhatsApp\n"
        ),
    }

    SUBTASKS = [SUBTASK_UNICA]

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
       
    logger.info(f"Etapa 3A iniciada - {project['company_name']} - Task-Id: {task_id}")
    return task_id