def generate_book_ideas():
    trends = [
        {"genre": "Science-Fiction", "trend": "Künstliche Intelligenz", "target": "Jugendliche", "style": "spannend, futuristisch"},
        {"genre": "Self-Help", "trend": "Achtsamkeit", "target": "Erwachsene", "style": "ruhig, motivierend"}
    ]
    ideas = []
    for t in trends:
        idea = {
            "title": f"Buch über {t['trend']}",
            "description": f"Ein {t['genre']}-Buch für {t['target']} im Stil {t['style']}",
            "style": t["style"],
            "source": "ScoutBot Trendanalyse"
        }
        ideas.append(idea)
    return ideas
