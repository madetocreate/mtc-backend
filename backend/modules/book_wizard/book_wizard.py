"""Buch-Wizard Modul: Erzeugt Kapitel aus Prompts."""
from .prompts import load_prompt
from .db import save_project
from .memory import append_to_memory
    """Erzeugt ein Buchkapitel basierend auf Nutzereingaben und Template."""
from .memory_log import log_chapter_to_memory

def generate_chapter(data):
    prompt = load_prompt("chapter_prompt.txt")
    filled_prompt = prompt.format(**data)
    save_project(data, filled_prompt)
    append_to_memory("chapters", {
        "title": data.get("title"),
        "chapter": data.get("chapter_number"),
        "heading": data.get("chapter_title"),
        "style": data.get("style"),
        "audience": data.get("audience"),
        "text": filled_prompt
    })
    log_chapter_to_memory(data, filled_prompt)
    return filled_prompt
