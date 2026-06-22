from core.database import supabase

result = supabase.table("employees").select("*").execute()

for employee in result.data:
    print(f"{employee['name']}: {employee['role']}")