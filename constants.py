# Project Status
from datetime import datetime, timedelta


class ProjectStatus:
    ACTIVE = "active"
    PAUSED = "paused"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

# Project Stages
class Stages:
    STAGE_1 = "stage_1"
    STAGE_2 = "stage_2"
    STAGE_3A = "stage_3_a"
    STAGE_3B = "stage_3_b"
    STAGE_3C = "stage_3_c"
    STAGE_3D = "stage_3_d"
    STAGE_4A = "stage_4_a"
    STAGE_4B = "stage_4_b"
    FINAL_STAGE = "final_stage"

# Project Pipelines
class TaskStatus:
    ABERTAS = "ABERTAS"
    AGUARDANDO_RESPOSTA = "AGUARDANDO RESPOSTA"
    REUNIOES_PEDRO = "REUNIÕES PEDRO"
    REUNIOES_KAUAN = "REUNIÕES KAUAN"
    TAREFAS_CS = "TAREFAS DO CS"
    TAREFAS_DEV = "TAREFAS DESENVOLVEDORES"
    PERSONALIZAR_CRM = "PERSONALIZAR CRM - CS"
    PROJETO_FINALIZADO = "PROJETO FINALIZADO"

# Employeers Roles
class EmployeeRoles:
    DEV = "Desenvolvedor"
    CS = "Customer Sucess"
    GESTOR = "Gestor de Projetos"

# ClickUp Members ID
class ClickUpMembers:
    PEDRO     = 72844227
    ISAAC     = 111975410
    VITOR_AGUIAR   = 111975411   
    KAUAN     = 111975463
    FELIPE    = 118035447
    VITOR_GUEDSON   = 118065770 

# Roles/Assignees Mapping
class RoleAssignees:
    CS = [ClickUpMembers.VITOR_GUEDSON]
    GESTOR = [ClickUpMembers.KAUAN]
    DEVS = [
        ClickUpMembers.ISAAC,
        ClickUpMembers.VITOR_AGUIAR,
        ClickUpMembers.FELIPE,
    ]

# Objetc to get due_date in timestamp format
def get_due_date(days: int) -> int:
    due = datetime.now()
    days_added = 0
    while days_added < days:
        due += timedelta(days=1)
        if due.weekday() < 5:  # 0=Seg ... 4=Sex, 5=Sab, 6=Dom
            days_added += 1
    return int(due.timestamp() * 1000)