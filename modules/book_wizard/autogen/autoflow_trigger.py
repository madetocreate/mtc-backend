from creator_engine.modules.book_wizard.autogen.full_autoflow import run_full_autoflow
from creator_engine.modules.book_wizard.memory_log import log_chapter_to_memory

def run_autoflow_for_buchideen():
    book_title = "Mein erstes Buch"
    style = "informativ"
    result = run_full_autoflow(book_title, style)
    # Kapitel speichern
    for chapter_title, content in result.items():
        log_chapter_to_memory({"book_title": book_title, "chapter_title": chapter_title}, content)
    return result
