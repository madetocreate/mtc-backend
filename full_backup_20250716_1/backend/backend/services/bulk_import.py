from dependencies.supabase_client import get_supabase_client

async def bulk_import(data_list):
    sb = get_supabase_client()
    for chunk in [data_list[i:i+20] for i in range(0, len(data_list), 20)]:
        sb.table("memory").insert(chunk).execute()
    return {"bulk": "ok"}
