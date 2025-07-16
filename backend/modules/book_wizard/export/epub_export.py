"""EPUB-Exportmodul für Buchdaten"""
from ebooklib import epub

def export_epub(data):
    """Erzeugt und speichert ein EPUB aus Buchdaten."""
    book = epub.EpubBook()
    book.set_title(data.get("title", "Unbekanntes Buch"))
    book.add_author(data.get("author", "Unbekannter Autor"))

    chapter = epub.EpubHtml(title="Kapitel 1", file_name="chap_01.xhtml", lang="de")
    chapter.content = data.get("content", "<h1>Kein Inhalt</h1>")
    book.add_item(chapter)

    book.toc = (epub.Link('chap_01.xhtml', 'Kapitel 1', 'chap1'),)
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    output_path = data.get("output_path", "output.epub")
    epub.write_epub(output_path, book)
    return output_path

