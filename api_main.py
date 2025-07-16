from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API läuft ✅"}

@app.post("/claude")
async def claude_handler(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "")
    return JSONResponse(content={"response": f"Claude sagt: {prompt}"})
from modules.memory import api as memory_api
app.include_router(memory_api.router)

@app.get("/memory/buchideen")
def get_buchideen():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    buchideen = memory.get("buchideen", [])
    return [{"title": e.get("title", "Untitled"), "content": e.get("content", "")} for e in buchideen[-20:]]

@app.get("/memory/buchideen")
def get_buchideen():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    buchideen = memory.get("buchideen", [])
    return [{"title": e.get("title", "Untitled"), "content": e.get("content", "")} for e in buchideen[-20:]]

@app.get("/memory/buchideen")
def get_buchideen():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    buchideen = memory.get("buchideen", [])
    return [{"title": e.get("title", "Untitled"), "content": e.get("content", "")} for e in buchideen[-20:]]

@app.get("/memory/buchideen")
def api_get_buchideen():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    buchideen = memory.get("buchideen", [])
    return [{"title": e.get("title", "Untitled"), "content": e.get("content", "")} for e in buchideen[-20:]]

@app.get("/memory/buchideen")
def get_buchideen():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    buchideen = memory.get("buchideen", [])
    return [{"title": e.get("title", "Untitled"), "content": e.get("content", "")} for e in buchideen[-30:]]

@app.get("/memory/{category}")
def get_memory_category(category: str):
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    return memory.get(category, [])

@app.get("/memory/all")
def get_memory_all():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    all_entries = []
    for cat, items in memory.items():
        for item in items:
            item["metadata"]["category"] = cat
            all_entries.append(item)
    return all_entries

import os
from fastapi.responses import JSONResponse

@app.get("/exports/list")
def list_exports():
    export_dir = "public/exports"
    if not os.path.exists(export_dir):
        return JSONResponse(content=[])
    files = os.listdir(export_dir)
    return JSONResponse(content=files)

import os
from fastapi.responses import JSONResponse

@app.get("/exports/list")
def list_exports():
    export_dir = "public/exports"
    if not os.path.exists(export_dir):
        return JSONResponse(content=[])
    files = os.listdir(export_dir)
    return JSONResponse(content=files)

import os
from fastapi.responses import JSONResponse

@app.get("/exports/list")
def list_exports():
    export_dir = "public/exports"
    if not os.path.exists(export_dir):
        return JSONResponse(content=[])
    files = os.listdir(export_dir)
    return JSONResponse(content=files)

from fastapi import Request

@app.post("/recherche/auftrag")
async def new_recherche_auftrag(request: Request):
    data = await request.json()
    query = data.get("query")
    domain = data.get("domain", "all")
    from creator_engine.modules.scoutbot.scout import scout_recherche
    result = scout_recherche(query, domain)
    return {"message": result}

from fastapi.responses import JSONResponse

@app.post("/autoflow/start")
async def start_autoflow():
    from creator_engine.modules.book_wizard.autogen.autoflow_trigger import run_autoflow_for_buchideen
    import threading
    def run_in_thread():
        run_autoflow_for_buchideen()
    threading.Thread(target=run_in_thread, daemon=True).start()
    return JSONResponse(content={"message": "AutoFlow gestartet"})

from creator_engine.modules.scheduler.cron import schedule_autoflow

@app.on_event("startup")
async def startup_event():
    schedule_autoflow(interval_seconds=86400)  # Täglich automatisch AutoFlow starten

@app.get("/memory/export")
def export_memory():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    # Später: Export als JSON/CSV/PDF etc.
    return memory

@app.get("/memory/export")
def export_memory():
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    # Später: Export als JSON/CSV/PDF etc.
    return memory

from fastapi import Request

@app.post("/memory/save")
async def save_memory(request: Request):
    data = await request.json()
    category = data.get("category")
    content = data.get("content")
    metadata = data.get("metadata", {})
    from creator_engine.modules.memory.memory_bridge import memory_save
    entry = memory_save(category, content, metadata)
    return {"status": "ok", "entry": entry}

@app.get("/memory/read/{category}")
def read_memory_category(category: str):
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    return memory.get(category, [])

from fastapi import Body

@app.post("/chat/memory/save")
async def chat_memory_save(data: dict = Body(...)):
    from creator_engine.modules.memory.memory_bridge import memory_save
    category = data.get("category")
    content = data.get("content")
    metadata = data.get("metadata", {})
    entry = memory_save(category, content, metadata)
    return {"status": "ok", "entry": entry}

@app.get("/chat/memory/read/{category}")
def chat_memory_read(category: str):
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    return memory.get(category, [])

from creator_engine.modules.scheduler.memory_cleanup import schedule_cleanup

@app.on_event("startup")
async def startup_event():
    schedule_cleanup(interval_seconds=86400)

from fastapi import Query

@app.get("/memory/search/{category}")
def search_memory_category(category: str, keyword: str = Query(...)):
    from creator_engine.modules.memory.core import read_memory
    memory = read_memory()
    entries = memory.get(category, [])
    results = [e for e in entries if keyword.lower() in e.get("content", "").lower()]
    return results

from creator_engine.modules.scheduler.cron import schedule_autoflow
from creator_engine.modules.scheduler.memory_cleanup import schedule_cleanup

@app.on_event("startup")
async def startup_event():
    schedule_autoflow(interval_seconds=86400)
    schedule_cleanup(interval_seconds=86400)

from creator_engine.modules.scheduler.memory_cleanup import schedule_cleanup

@app.on_event("startup")
async def startup_event():
    schedule_cleanup(interval_seconds=86400)
