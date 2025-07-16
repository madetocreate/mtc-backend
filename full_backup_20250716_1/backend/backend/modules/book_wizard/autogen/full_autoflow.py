from creator_engine.modules.book_wizard.autogen.structure_generator import generate_structure
from creator_engine.modules.book_wizard.autogen.chapter_writer import write_chapter
from creator_engine.modules.book_wizard.memory_log import log_chapter_to_memory

def run_full_autoflow(book_title, style="neutral"):
    structure = generate_structure(book_title, style)
    chapters = structure.split('\\n')
    book_content = {}
    for chapter in chapters:
        content = write_chapter(book_title, chapter, style)
        book_content[chapter] = content
        log_chapter_to_memory({"book_title": book_title, "chapter_title": chapter}, content)
    return book_content
