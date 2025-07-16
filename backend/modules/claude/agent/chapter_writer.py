import openai, os
def write_chapter(book_title, genre, chapter_title):
    with open("../modules/claude/agent/prompts/chapter_template.txt") as t: prompt = t.read().format(chapter_title=chapter_title, book_title=book_title, genre=genre)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    resp = openai.ChatCompletion.create(model="gpt-4o", messages=[{"role": "user", "content": prompt}])
    text = resp.choices[0].message.content
    path = f"../modules/books/{book_title.replace(' ', '_')}_{chapter_title.replace(' ', '_')}.md"
    with open(path, "w") as f: f.write(text)
    print(f"Kapitel {chapter_title} gespeichert unter: {path}")

