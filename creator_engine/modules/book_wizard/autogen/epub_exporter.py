from ebooklib import epub

def export_epub(title, content, metadata=None):
    book = epub.EpubBook()
    book.set_title(title)
    book.set_language('de')
    book.add_author(metadata.get("autor", "Auto-GPT"))

    chapter = epub.EpubHtml(title='Inhalt', file_name='chap_1.xhtml', lang='de')
    chapter.content = f"<h1>{title}</h1><p>{content.replace('\n', '<br/>')}</p>"
    book.add_item(chapter)
    book.spine = ['nav', chapter]

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    filename = f"public/exports/{title.replace(' ', '_')}.epub"
    epub.write_epub(filename, book)
    return filename
