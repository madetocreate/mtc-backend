from pathlib import Path

def save_chapter(project, chapter_num, chunks):
    path = Path(f"books/{project}/kapitel_{chapter_num:02}.md")
    with open(path, "w") as f:
        for chunk in chunks:
            f.write(chunk + "\n\n")
