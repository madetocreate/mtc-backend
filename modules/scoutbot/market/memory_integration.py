import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from creator_engine.modules.memory.memory_bridge import memory_save
from creator_engine.modules.scoutbot.market.book_idea_generator import generate_book_ideas

def save_book_ideas_to_memory():
    ideas = generate_book_ideas()
    for idea in ideas:
        memory_save("buchideen", idea["description"], {
            "title": idea["title"],
            "style": idea["style"],
            "source": idea["source"]
        })
