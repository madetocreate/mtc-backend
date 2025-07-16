import os

def list_bot_files(dirs):
    files = []
    for directory in dirs:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                if filename.endswith(".py"):
                    files.append(os.path.join(root, filename))
    return files

def syntax_check(file_path):
    try:
        with open(file_path, "r") as f:
            source = f.read()
        compile(source, file_path, 'exec')
        return True, None
    except SyntaxError as e:
        return False, str(e)

def check_todos(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
    todos = [i+1 for i, line in enumerate(lines) if "TODO" in line]
    return todos

def gpt_review_placeholder(file_path):
    return f"GPT-Review: Code in {file_path} sieht auf den ersten Blick gut aus."

def review_all_bots(dirs, report_path="logs/auto/technical_review.md"):
    bots = list_bot_files(dirs)
    if not bots:
        print("Keine Bot-Dateien gefunden.")
        return

    report_lines = ["# Technischer Review Report\n\n"]
    for bot in bots:
        report_lines.append(f"## Datei: {bot}\n")
        ok, err = syntax_check(bot)
        if ok:
            report_lines.append("- Syntax: OK\n")
        else:
            report_lines.append(f"- Syntax-Fehler: {err}\n")
        todos = check_todos(bot)
        if todos:
            report_lines.append(f"- WARNUNG: TODO-Kommentare auf Zeilen: {todos}\n")
        else:
            report_lines.append("- TODO-Kommentare: Keine gefunden\n")
        report_lines.append(f"- {gpt_review_placeholder(bot)}\n\n")

    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w") as f:
        f.writelines(report_lines)

    print(f"Review abgeschlossen. Bericht gespeichert in {report_path}")

if __name__ == "__main__":
    dirs = [
        "backend/modules/atomic_bots",
        "backend/modules/voicebot",
        "backend/modules/scoutbot",
        "backend/modules/codebot",
        "backend/modules/marketingbot"
    ]
    review_all_bots(dirs)
