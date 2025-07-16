from fastapi import APIRouter, Request
from ..book_wizard import book_wizard
from ..book_wizard.db import get_all_projects

router = APIRouter()

@router.post("/api/bookwizard/chapter")
async def create_chapter(request: Request):
    data = await request.json()
    result = book_wizard.generate_chapter(data)
    return {"output": result}

@router.get("/api/bookwizard/projects")
async def list_projects():
    projects = get_all_projects()
    return {"projects": projects}

@router.get("/api/bookwizard/export")
async def export_project(id: int):
    import sqlite3
    from ..book_wizard.db import DB_PATH
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT output FROM projects WHERE id = ?", (id,))
        row = c.fetchone()
        return {"output": row[0] if row else ""}

