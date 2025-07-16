import openai
import os
from chapter_writer import write_chapter
from memory_handler import save_book_to_memory

def write_book(title, genre, extra=""):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Schreibe ein vollständiges Buch mit dem Titel '{title}' im Genre '{genre}'. {extra}"
    resp = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    book_text = resp.choices[0].message.content
    book_path = f"../modules/books/{title.replace(' ', '_')}.md"
    with open(book_path, "w") as f:
        f.write(book_text)
    print(f"Buch gespeichert unter: {book_path}")
    save_book_to_memory(title, book_text)

def write_book_with_chapters(title, genre, chapters):
    full_text = f"# {title}\n\n"
    for chap in chapters:
        write_chapter(title, genre, chap)
        chapter_path = f"../modules/books/{title.replace(' ', '_')}_{chap.replace(' ', '_')}.md"
        with open(chapter_path) as f:
            full_text += f"\n## {chap}\n" + f.read() + "\n"
    book_path = f"../modules/books/{title.replace(' ', '_')}.md"
    with open(book_path, "w") as f:
        f.write(full_text)
    print(f"Buch mit Kapiteln gespeichert unter: {book_path}")
    save_book_to_memory(title, full_text)
