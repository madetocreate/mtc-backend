from full_writer import autoflow_full_book
from epub_exporter import export_epub

title = "Die Kraft der Achtsamkeit"
style = "achtsam, ruhig, sanft"
book = autoflow_full_book(title, style)

pfad = export_epub(title, book, {"autor": "Auto-GPT"})
print("EPUB gespeichert unter:", pfad)
