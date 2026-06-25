from core.logger import get_logger

logger = get_logger(__name__)

# Create checkpoint task
def checkpoint() -> None:

    logger.info(f"Projeto finalizado(Somente Acompanhamento) - {project['company_name']}")

