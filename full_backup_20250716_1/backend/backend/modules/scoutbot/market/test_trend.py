from .trend_scout import get_book_trends
from .bookidea_builder import build_book_idea
from modules.scoutbot.market.memory_writer import write_idea_to_memory

def run_trend_pipeline():
    trends = get_book_trends()
    for trend in trends:
        idea = build_book_idea(trend)
        write_idea_to_memory(idea)
        print(f"Idee gespeichert: {idea['title']}")

if __name__ == "__main__":
    run_trend_pipeline()
