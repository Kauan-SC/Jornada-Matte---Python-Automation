from constants import Stages
from core.database import get_completed_projects_by_stage
from core.logger import get_logger
from stages.stage_follow_up.validacao.validacao import validacao

logger = get_logger(__name__)

# Check if projets are in Final Stage
def validacao_check() -> None:

    projects = get_completed_projects_by_stage(Stages.FINAL_STAGE_IA)

    for project in projects:
        validacao(project)
