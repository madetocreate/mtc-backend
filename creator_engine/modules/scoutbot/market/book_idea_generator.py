from creator_engine.modules.scoutbot.market.trend_analysis import get_book_trends

def generate_book_ideas():
    trends = get_book_trends()
    ideas = []
    for t in trends:
        idea = {
            "title": f\"Buch über {t['trend']}\",
            "description": f\"Ein {t['genre']}-Buch für {t['target']} im Stil {t['style']}\",
            "style": t["style"],
            "source": "ScoutBot Trendanalyse"
        }
        ideas.append(idea)
    return ideas
