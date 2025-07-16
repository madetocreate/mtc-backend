def is_relevant(task):
    keywords = ["NLP", "Thriller", "Roman", "Claude", "GPT", "Kapitel", "Export"]
    return any(kw.lower() in task.lower() for kw in keywords)
