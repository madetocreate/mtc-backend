from fastapi import APIRouter
import sqlite3

router = APIRouter()
DB_PATH = "db/creator_engine.db"

@router.get("/logs")
def get_logs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT module, message, created_at FROM ai_logs ORDER BY id DESC LIMIT 20")
    rows = cursor.fetchall()
    return {"logs": [{"module": r[0], "message": r[1], "created_at": r[2]} for r in rows]}
