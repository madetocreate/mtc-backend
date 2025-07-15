from ebooklib import epub
import os

def export_as_epub(title, chapters):
    book = epub.EpubBook()
    book.set_identifier(title.replace(' ', '_'))
    book.set_title(title)
    book.set_language('de')

    spine = ['nav']
    toc = []

    for i, ch in enumerate(chapters):
        c = epub.EpubHtml(title=ch['title'], file_name=f'chap_{i}.xhtml', lang='de')
        c.content = f'<h1>{ch["title"]}</h1><p>{ch["text"].replace("\n", "<br/>")}</p>'
        book.add_item(c)
        spine.append(c)
        toc.append(c)

    book.toc = tuple(toc)
    book.spine = spine
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    os.makedirs('public/exports', exist_ok=True)
    filename = f'public/exports/{title.replace(" ", "_")}.epub'
    epub.write_epub(filename, book)
    return filename
