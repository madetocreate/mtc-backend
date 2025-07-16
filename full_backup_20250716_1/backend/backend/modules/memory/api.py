from fastapi import APIRouter, Request
from .core import append_entry, get_entries, search_memory

router = APIRouter()

@router.post("/api/memory/add")
async def add_memory(request: Request):
    body = await request.json()
    category = body.get("category")
    content = body.get("content")
    metadata = body.get("metadata")
    result = append_entry(category, content, metadata)
    return {"status": "ok", "entry": result}

@router.get("/api/memory/latest")
async def latest_memory(category: str = "general"):
    return {"entries": get_entries(category)}

@router.get("/api/memory/search")
async def search(keyword: str, category: str = None):
    return {"results": search_memory(keyword, category)}

@router.post("/api/memory/add_task")
async def add_task_endpoint(request: Request):
    body = await request.json()
    from .tasks import add_task
    return {"status": "ok", "task": add_task(body.get("name"), body.get("desc"))}

@router.post("/api/memory/add_template")
async def add_template_endpoint(request: Request):
    body = await request.json()
    from .templates import save_template
    return {"status": "ok", "template": save_template(body.get("title"), body.get("text"))}
@router.get("/api/memory/delete")
async def delete_entry(id: str):
    from .core import read_memory, write_memory
    mem = read_memory()
    for cat in mem:
        mem[cat] = [e for e in mem[cat] if e["id"] != id]
    write_memory(mem)
    return {"status": "deleted"}
@router.get("/api/memory/export")
async def export_all():
    from .core import read_memory
    return read_memory()

@router.post("/api/memory/import")
async def import_all(request: Request):
    body = await request.json()
    from .core import write_memory
    write_memory(body)
    return {"status": "imported"}
