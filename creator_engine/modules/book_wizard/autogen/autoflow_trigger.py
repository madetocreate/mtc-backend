import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from creator_engine.modules.memory.core import read_memory
from creator_engine.modules.book_wizard.autogen.full_autoflow import full_autoflow
from creator_engine.modules.book_wizard.export.epub_export import export_as_epub

def run_autoflow_for_buchideen():
    memory = read_memory()
    buchideen = memory.get("buchideen", [])
    for idee in buchideen:
        title = idee.get("title")
        style = idee.get("style", "neutral")
        print(f"Starte AutoFlow für: {title} (Stil: {style})")
        buch_text = full_autoflow(title, style)
        epub_path = export_as_epub(title, [{"title": "Gesamtes Buch", "text": buch_text}])
        print(f"EPUB erstellt: {epub_path}")

if __name__ == "__main__":
    run_autoflow_for_buchideen()
