import sqlite3
import os

DB_PATH = os.path.join("db", "book_projects.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            chapter_number TEXT,
            chapter_title TEXT,
            previous_summary TEXT,
            style TEXT,
            audience TEXT,
            output TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""")
        conn.commit()

def save_project(data, output):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("""INSERT INTO projects 
        (title, chapter_number, chapter_title, previous_summary, style, audience, output) 
        VALUES (?, ?, ?, ?, ?, ?, ?)""", (
            data.get("title"),
            data.get("chapter_number"),
            data.get("chapter_title"),
            data.get("previous_summary"),
            data.get("style"),
            data.get("audience"),
            output
        ))
        conn.commit()

def get_all_projects():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT id, title, chapter_number, chapter_title, created_at FROM projects ORDER BY created_at DESC")
        return c.fetchall()

