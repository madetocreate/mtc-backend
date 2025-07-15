from creator_engine.modules.book_wizard.autogen.structure_generator import generate_structure
from creator_engine.modules.book_wizard.autogen.chapter_writer import write_chapter
from creator_engine.modules.memory.memory_bridge import memory_save

def full_autoflow(title, style="neutral"):
    structure_text = generate_structure(title, style)
    memory_save("buchstruktur", structure_text, {"title": title})
    chapters = [line.strip() for line in structure_text.split("\n") if line.strip()]
    full_book = ""
    for chapter_title in chapters:
        chapter_text = write_chapter(title, chapter_title, style)
        memory_save("kapitel", chapter_text, {"chapter": chapter_title, "title": title})
        full_book += f"# {chapter_title}\n\n{chapter_text}\n\n"
    return full_book

def autoflow_from_memory():
    from creator_engine.modules.memory.core import read_memory
    ideas = read_memory().get("buchideen", [])
    results = []
    for idea in ideas:
        title = idea.get("title")
        style = idea.get("style", "neutral")
        book_text = full_autoflow(title, style)
        results.append((title, book_text))
    return results
