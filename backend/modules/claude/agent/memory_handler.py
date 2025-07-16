import os
def save_book_to_memory(book_title, text):
    path = f"../modules/memory/books/{book_title.replace(' ', '_')}_memory.md"
    with open(path, "w") as f: f.write(text)
    print(f"Buch in Memory gespeichert: {path}")
