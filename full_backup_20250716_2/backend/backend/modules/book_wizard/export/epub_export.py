from ebooklib import epub
import os

def export_as_epub(title, chapters, output_dir="public/exports"):
    book = epub.EpubBook()
    book.set_identifier("id123456")
    book.set_title(title)
    book.set_language("de")

    book.add_author("Anima Collective")

    epub_chapters = []
    for i, chap in enumerate(chapters, start=1):
        c = epub.EpubHtml(title=chap["title"], file_name=f'chap_{i}.xhtml', lang='de')
        c.content = f"<h1>{chap['title']}</h1><p>{chap['text'].replace('\\n', '<br/>')}</p>"
        book.add_item(c)
        epub_chapters.append(c)

    book.toc = tuple(epub_chapters)
    book.spine = ['nav'] + epub_chapters
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_path = os.path.join(output_dir, f"{title.replace(' ', '_')}.epub")
    epub.write_epub(file_path, book)
    return file_path
