import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from modules.scoutbot.market.memory_integration import save_book_ideas_to_memory

if __name__ == "__main__":
    save_book_ideas_to_memory()
    print("✅ Buchideen in Memory gespeichert")
