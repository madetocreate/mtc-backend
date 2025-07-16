import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

import importlib.util

epub_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'epub_export.py'))
spec = importlib.util.spec_from_file_location("epub_export", epub_path)
epub_export = importlib.util.module_from_spec(spec)
spec.loader.exec_module(epub_export)

chapters = [
    {"title": "Kapitel 1", "text": "Dies ist das erste Kapitel."},
    {"title": "Kapitel 2", "text": "Dies ist das zweite Kapitel."}
]

pfad = epub_export.export_as_epub("Testbuch", chapters)
print(f"✅ EPUB gespeichert unter: {pfad}")
