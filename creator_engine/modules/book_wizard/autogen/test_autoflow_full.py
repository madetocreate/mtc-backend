from full_autoflow import full_autoflow
from epub_export import export_as_epub
from pdf_export import export_as_pdf

title = "Mega Buch"
style = "inspirierend"

book_text = full_autoflow(title, style)

epub_path = export_as_epub(title, [{"title": "Gesamtes Buch", "text": book_text}])
pdf_path = export_as_pdf(title, book_text)

print(f"EPUB gespeichert unter: {epub_path}")
print(f"PDF gespeichert unter: {pdf_path}")
