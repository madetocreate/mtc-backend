from creator_engine.modules.book_wizard.autogen.structure_generator import generate_structure
from creator_engine.modules.book_wizard.autogen.chapter_writer import write_chapter
from creator_engine.modules.memory.memory_bridge import memory_save

def autoflow_full_book(title, style="neutral"):
    structure = generate_structure(title, style)
    memory_save("buchstruktur", structure, {"title": title})
    chapters = [line.strip() for line in structure.split("\n") if line.strip()]
    content = ""
    for ch in chapters:
        chapter = write_chapter(title, ch, style)
        memory_save("kapitel", chapter, {"chapter": ch, "title": title})
        content += f"# {ch}\n\n{chapter}\n\n"
    return content
