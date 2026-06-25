from constants import Stages
from core.database import get_active_projects_by_stage
from core.logger import get_logger

logger = get_logger(__name__)

# Check if projets are in Final Stage
def validacao_check() -> None:

    projetos_crm = get_active_projects_by_stage(Stages.FINAL_STAGE_CRM)
    projetos_ia = get_active_projects_by_stage(Stages.FINAL_STAGE_IA)

    if projetos_crm and projetos_ia:




        
