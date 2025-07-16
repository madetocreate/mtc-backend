def launch_bookbot_task():
    from modules.atomic_bots.bookbot.generator import generate_chapter
    chapter = generate_chapter()
    open("output/bookbot/ch1.md", "w").write(chapter)
    print("✅ Kapitel generiert")
