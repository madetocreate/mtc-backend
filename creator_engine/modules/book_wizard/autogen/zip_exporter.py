import zipfile, os

def export_zip(title, content, metadata=None):
    safe_title = title.replace(" ", "_")
    zip_path = f"public/exports/{safe_title}.zip"
    txt_path = f"{safe_title}.txt"
    meta_path = f"{safe_title}_meta.txt"

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(content)

    if metadata:
        with open(meta_path, "w", encoding="utf-8") as f:
            for k, v in metadata.items():
                f.write(f"{k}: {v}\n")

    with zipfile.ZipFile(zip_path, 'w') as zipf:
        zipf.write(txt_path)
        if metadata: zipf.write(meta_path)

    os.remove(txt_path)
    if metadata: os.remove(meta_path)
    return zip_path
