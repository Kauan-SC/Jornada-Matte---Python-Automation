from datetime import datetime, timezone

from constants import ProjectStatus, RoleAssignees, Stages, TaskStatus, get_due_date
from core.database import supabase
from core.logger import get_logger
from integrations.clickup import create_subtask, create_task

logger = get_logger(__name__)

# ETAPA: 1 - Boas-Vindas, Apresentação da Equipe, Feedback da Reunião de Vendas e Marcar Onboarding com Cliente

def run(client_name: str, company_name: str, service_description: str) -> dict | None:

    # Histórico do projeto no log
    logger.info(f"Etapa 1 Iniciada - {company_name}")

    # Data de vencimento da tarefa, 3 dias a partir da criação
    data = get_due_date(3)

    # Criar a tarefa principal no ClickUp
    task = create_task(
        name=f"Primeiro Passo de - {company_name}",
        status=TaskStatus.TAREFAS_CS,
        description=(
            f"O cliente {client_name} iniciou o projeto\n\n\n"
            f"Os próximos passos são:\n"
            f"Boas-Vindas\n"
            f"Apresentação da Equipe\n"
            f"Feedback da Reunião de Vendas\n"
            f"Marcar Onboarding com Cliente"),
        assignees=RoleAssignees.CS,
        due_date=data
    )

    # Se a tarefa não for criada, logar o erro e retornar None
    if task is None:
        logger.error(f"Erro na Etapa 1 - Empresa {company_name}, Cliente {client_name}")
        return None
    
    task_id = task["id"]

# ----------------------------------------------------------------------------------------------------------------------------------------------

    # Dados de cada subtarefa
    BOAS_VINDAS = {
        "name": "Boas-Vindas",
        "description": (
            "1- Adicionar todos ao grupo\n"
            "2- Dar as Boas vindas para o cliente:\n\n"
            "Boa tarde cliente!\n"
            "Sejam muito bem vindos e parabéns pela decisão.🎉🎉🎉🚀🚀🚀"
        ),
    }

    APRESENTACAO_EQUIPE = {
        "name": "Apresentação da Equipe",
        "description": (
            "3- Apresentar a equipe:\n\n\n"
            "Gostaria de apresentar oficialmente nosso time:\n\n"
            "🚀 Estratégia e Liderança: @Pedro , nosso Founder, acompanhará o projeto de perto com você.\n\n"
            "🤝 Comercial: @Joao, @Felipe e @Negrete.\n"
            "📱 Marketing & Social: @Joao Social Selling.\n\n"
            "⚙️ Tecnologia: @Felipe , @Vitor e @Isaac são nossa célula de TI dedicada.\n\n"
            "📋 Gestão e Sucesso: Eu sou o Gestor de Projetos e o @Virtao CS do time, "
            "e estaremos ao seu lado durante toda a jornada para garantir os melhores resultados."
        ),
    }

    FEEDBACK_REUNIAO = {
        "name": "Feedback da Reunião de Vendas",
        "description": (
            "1- Enviar para o privado do cliente esse link para que ele possa avaliar a reunião de venda\n\n\n"
            "Oi! Tudo bem? 😊\n"
            "Mandando mensagem aqui, para saber oque achou da reunião de Vendas que realizou com o Pedro/Joao!\n\n"
            "Isso ajuda nosso time a evoluir e atender cada vez melhor!\n\n"
            "Pedimos apenas 1 minutinho do seu tempo para avaliar como foi a conversa:\n"
            "👉 https://agenda.mattefunnelpro.com/widget/survey/ANK5u0eMnuYhv62glrDa\n\n"
            "Sua opinião faz toda a diferença para nós. Obrigado!"
        ),
    }

    MARCAR_ONBOARDING = {
        "name": "Marcar Onboarding com Cliente",
        "description": (
            "1- Marcar o Onboarding de Apresentação com o cliente\n\n"
            "O primeiro passo é agendarmos nosso Onboarding e dar início ao projeto.\n\n"
            "O objetivo desse encontro é alinhar tudo para o sucesso da operação:\n\n"
            "🚀 Acesso aos materiais exclusivos para acelerar seus resultados;\n\n"
            "🤖 Apresentação do Briefing da IA;\n\n"
            "✅ Definição dos próximos passos para colocar sua operação no piloto automático.\n\n"
            "Vocês preferem o período da manhã ou da tarde?\n\n"
            "Qualquer dúvida antes da reunião, é só chamar por aqui.\n\n"
            "Nos vemos em breve para iniciar essa transformação!"
        ),
    }

    SUBTASKS = [
        BOAS_VINDAS,
        APRESENTACAO_EQUIPE,
        FEEDBACK_REUNIAO,
        MARCAR_ONBOARDING,
    ]

# ----------------------------------------------------------------------------------------------------------------------------------------------

    # Criar as subtarefas no ClickUp
    for subtask in SUBTASKS:
        create_subtask(
            parent_task_id=task_id,
            name=subtask["name"],
            description=subtask.get("description", ""),
            assignees=RoleAssignees.CS,
            due_date=data
        )


    # Salvar o projeto no Supabase
    try:
            supabase.table("projects").insert({
                "client_name": client_name,
                "company_name": company_name,
                "task_id": task_id,
                "current_stage": Stages.STAGE_1,
                "status": ProjectStatus.ACTIVE,
                "created_at": datetime.now(timezone.utc).isoformat(),  
                "started_at": datetime.now(timezone.utc).isoformat(),
                "service_description": service_description,

            }).execute()

            # Se der certo, logar a informação de sucesso
            logger.info(f"Projeto - {company_name} salvo no Supabase - Task-Id: {task_id}")

    except Exception as e:

        # Se der erro, logar a informação de erro
        logger.error(f"Erro ao salvar Etapa 1 no Supabase - {company_name}: {e}")


        