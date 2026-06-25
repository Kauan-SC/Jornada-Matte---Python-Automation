# from constants import TaskStatus, get_due_date
# from core.logger import get_logger
# from integrations.clickup import create_task

# logger = get_logger(__name__)

# def create_final_stage(project: dict) -> str | None:

#     logger.info(f"Projeto finalizado(Somente Acompanhamento) - {project['company_name']}")

#     data = get_due_date(40)

#     # Create Task - Final Stage
#     task = create_task(
#         name=f"Acompanhamento Após 30 dias - {project['company_name']}",
#         status=TaskStatus.PROJETO_FINALIZADO,
#         description=(
#         "- Verificar andamento e funcionamento do projeto do cliente\n"
#         "- Confirmar satisfação do cliente\n"
#         "- Coletar feedback\n"
#         "- Se positivo: solicitar indicação"),
#         due_date=data
#     )

#     if task is None:
#         logger.error(f"Erro na Etapa Final - {project['company_name']}")
#         return None
    
#     task_id = task["id"]
#     logger.info(f"Etapa Final iniciada - {project['company_name']} - Task-Id: {task_id}")
#     return task_id
