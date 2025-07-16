from creator_engine.modules.memory.memory_bridge import memory_save

def log_chapter_to_memory(chapter_data, content):
    category = "buchkapitel"
    metadata = {
        "book_title": chapter_data.get("book_title"),
        "chapter_title": chapter_data.get("chapter_title")
    }
    memory_save(category, content, metadata)
