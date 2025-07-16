def auto_tag(task):
    tags = []
    if "NLP" in task: tags.append("#nlp")
    if "Claude" in task: tags.append("#claude")
    if "Roman" in task: tags.append("#roman")
    if "Thriller" in task: tags.append("#thriller")
    return " ".join(tags)
