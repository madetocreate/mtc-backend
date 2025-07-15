def export_txt(title, content):
    filename = f"public/exports/{title.replace(' ', '_')}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename
