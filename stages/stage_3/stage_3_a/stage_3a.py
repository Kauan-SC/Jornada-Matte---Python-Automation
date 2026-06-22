from constants import RoleAssignees, TaskStatus, get_due_date
from core.logger import get_logger
from integrations.clickup import create_subtask, create_task

logger = get_logger(__name__)

def create_stage_3a(project: dict) -> str | None:

    logger.info(f"Etapa 3A Iniciada - {project['company_name']}")

    data = get_due_date(10)

    # Create Task - Third Step - A
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

    if task is None:
        logger.error(f"Erro na Etapa 3A - {project['company_name']}")
        return None
    
    task_id = task["id"]


    # Create Subtask - Third Step - A
    CADASTRO_LEADS = {
        "name": "Cadastro de Leads, Calendários e Horários",
        "description": (
            "Mensagem 1 — Leads:\n\n"
            "Boa tarde, @cliente! Dentro do CRM conseguimos importar e organizar todos os seus contatos.\n\n"
            "Se vocês já trabalharam com alguma lista de clientes ou usaram outro CRM, é só enviar aqui que fazemos a importação completa.\n\n"
            "────────────────────\n\n"
            "Mensagem 2 — Time:\n\n"
            "Além disso, para cadastrarmos os membros do time no sistema, precisamos do:\n"
            "Nome, Sobrenome, Telefone e E-mail de cada pessoa.\n\n"
            "────────────────────\n\n"
            "Mensagem 3 — Calendário:\n\n"
            "Também conseguimos integrar um calendário individual para cada membro do time(Para reuniões e outros), com disponibilidade personalizada para agendamentos.\n\n"
            "Vocês têm interesse em habilitar isso? Se sim, qual seria a disponibilidade ?"
        ),
    }

    CAPTACAO_LEADS = {
        "name": "Captação e Integração de Leads",
        "description": (
            "Pessoal, além dos contatos manuais, o CRM também recebe leads automaticamente via anúncios, sites e formulários.\n\n"
            "Vocês rodam campanhas na Meta (Facebook/Instagram) ou têm algum site ou formulário ativo?\n\n"
            "Se sim, conseguimos conectar tudo e criar um dashboard de leads direto no sistema."
        ),
    }

    AUTOMACOES = {
        "name": "Automações",
        "description": (
            "Boa tarde, pessoal!\n\n"
            "Para deixar o CRM ainda mais eficiente, conseguimos configurar:\n\n"
            "• Divisão automática de contatos entre os membros do time\n"
            "• Respostas automáticas para comentários e mensagens no Instagram, Facebook e TikTok\n\n"
            "Como podemos implementar isso para vocês?"
        ),
    }

    COMUNICACAO_CANAIS = {
        "name": "Comunicação e Canais",
        "description": (
            "Pessoal, a última etapa é conectar o WhatsApp de vocês ao CRM. Temos duas opções:\n\n"
            "1️⃣ API Oficial — $15 dólares/mês para a Meta + custo por disparo. Sem risco de bloqueio. Recomendado para maior volume de atendimento.\n\n"
            "2️⃣ WhatsApp Business — gratuito, funciona como o WhatsApp Web. Exige mais cuidado com volume de mensagens para evitar bloqueios.\n\n"
            "Qual das duas faz mais sentido para vocês?"
        ),
    }

    SUBTASKS = [CADASTRO_LEADS, CAPTACAO_LEADS, AUTOMACOES, COMUNICACAO_CANAIS]

    for subtask in SUBTASKS:
        create_subtask(
            parent_task_id=task_id,
            name=subtask["name"],
            description=subtask.get("description", ""),
            assignees=RoleAssignees.CS,
            due_date=data
        )
       
    logger.info(f"Etapa 3A iniciada - {project['company_name']} - Task-Id: {task_id}")
    return task_id