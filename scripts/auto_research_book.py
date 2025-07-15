from creator_engine.modules.scoutbot.scout import scout_recherche
from creator_engine.modules.book_wizard.autogen.full_autoflow import run_full_autoflow
from creator_engine.modules.book_wizard.memory_log import log_chapter_to_memory

def auto_research_and_write(book_title, research_query, style="neutral"):
    print(f"Starte Recherche zu '{research_query}'...")
    research_result = scout_recherche(research_query)
    print(f"Recherche Ergebnis: {research_result[:200]}...")

    print(f"Starte automatischen Schreib-Flow für Buch '{book_title}'...")
    book_content = run_full_autoflow(book_title, style)
    # Kapitel in Memory speichern
    for chapter, text in book_content.items():
        log_chapter_to_memory({"book_title": book_title, "chapter_title": chapter}, text)
    print("Buch-Erstellung abgeschlossen.")

if __name__ == "__main__":
    auto_research_and_write("Einführung in NLP", "Natural Language Processing", "klar und verständlich")
