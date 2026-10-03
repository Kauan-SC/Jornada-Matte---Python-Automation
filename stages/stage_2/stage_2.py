from constants import RoleAssignees, TaskStatus, get_due_date
from core.logger import get_logger
from integrations.clickup import create_subtask, create_task

logger = get_logger(__name__)

# ETAPA: 2 - Pós-Onboarding, Enviar Instruções de Criação de Conta no CRM e Feedback da Reunião de Onboarding

def create_stage_2(project: dict) -> str | None:

    logger.info(f"Etapa 2 Iniciada - {project['company_name']}")

    data = get_due_date(3)

# Cria a tarefa principal da Etapa 2 no ClickUp
    task = create_task(
        name=f"Pós-Onboarding de - {project['company_name']}",
        status=TaskStatus.TAREFAS_CS,
        description=(
            f"O cliente {project['client_name']} deu o segundo passo\n\n\n"
            f"Os próximos passos são:\n"
            f"Enviar instruções sobre criação de conta no CRM\n"
            f"Feedback da Reunião de Onboarding\n"),
        assignees=RoleAssignees.GESTOR,
        due_date=data
    )

    # Se a tarefa não for criada, logar o erro e retornar None
    if task is None:
        logger.error(f"Erro na Etapa 2 - {project['company_name']}")
        return None
    
    task_id = task["id"]

# ----------------------------------------------------------------------------------------------------------------------------------------------

    # Dados de cada subtarefa
    PROXIMOS_PASSOS = {
        "name": "Enviar instruções ao Cliente",
        "description":(
            "1- Enviar detalhes sobre criação da conta no CRM\n\n\n"
            "@Cliente para a gente começar a rodar o seu CRM, preciso que você finalize a assinatura no link abaixo:\n\n"
            "👉 https://ativar.magneticfunnels.io/conta-partner\n\n"    
            "🚨*ATENÇÃO*🚨\n"
            "Use o cupom *matte100* para ativar 12 meses de desconto na ferramenta.\n\n"
            "Qualquer dúvida na hora de preencher, me chama aqui.\n\n\n\n\n"
            "---------------------------------------\n\n\n"
            "2- Enviar segunda mensagem relembrando que é necessário o uso do cupom.\n\n\n"
            "*ATENÇÃO:* @Cliente, é necessário o uso do *CUPOM*\n"
            "O valor da compra precisa ser de R$0,00"
        ) 
    }

    SUBTASKS = [PROXIMOS_PASSOS]

# ----------------------------------------------------------------------------------------------------------------------------------------------

    # Criar cada subtarefa da Etapa 2 no ClickUp
    for subtask in SUBTASKS:
        create_subtask(
            parent_task_id=task_id,
            name=subtask["name"],
            description=subtask.get("description", ""),
            assignees=RoleAssignees.GESTOR,
            due_date=data
            )
       
    logger.info(f"Etapa 2 iniciada - {project['company_name']} - Task-Id: {task_id}")
    return task_id
       
