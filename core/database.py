from datetime import datetime

from supabase import Client, create_client

from config import SUPABASE_KEY, SUPABASE_URL

# Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Get all task determined in the stage
def get_active_projects_by_stage(stage: str) -> list[dict]:
    return (
        supabase.table("projects")
        .select("*")
        .eq("current_stage", stage)
        .eq("status", "active")
        .execute()
        .data
    )

# Update project status, ID and Stage
def update_project(project_id: str, new_stage: str, new_task_id: str, new_task_id_b: str | None = None) -> None:
    data = {
        "current_stage": new_stage,
        "task_id": new_task_id,
        "started_at": datetime.utcnow().isoformat(),
    }
    if new_task_id_b:
        data["task_id_b"] = new_task_id_b
    supabase.table("projects").update(data).eq("id", project_id).execute()

def insert_project_branch(original: dict, stage: str, task_id: str) -> None:
    supabase.table("projects").insert({
        "company_name": original["company_name"],
        "client_name": original.get("client_name", ""),
        "service_description": original.get("service_description", ""),
        "current_stage": stage,
        "task_id": task_id,
        "status": "active",
        "started_at": datetime.utcnow().isoformat(),
    }).execute()