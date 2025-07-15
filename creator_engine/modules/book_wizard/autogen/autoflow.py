from creator_engine.modules.book_wizard.autogen.structure_generator import generate_structure
from creator_engine.modules.memory.memory_bridge import memory_save

def autoflow_book_from_idea(idea):
    structure = generate_structure(idea["title"], idea.get("style", "neutral"))
    memory_save("buchstruktur", structure, {
        "quelle": "autoflow",
        "title": idea["title"]
    })
    return structure
