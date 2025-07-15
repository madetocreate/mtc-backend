def build_book_idea(trend_data):
    return {
        "title": f"AI-Risiko: {trend_data['trend']}",
        "description": f"Ein Buch über {trend_data['trend']} im Genre {trend_data['genre']}, für {trend_data['target']}.",
        "style": trend_data["style"],
        "source": trend_data["example"]
    }
