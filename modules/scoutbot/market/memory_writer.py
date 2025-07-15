import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from creator_engine.modules.memory.memory_bridge import memory_save

def write_idea_to_memory(idea):
    memory_save("buchideen", idea["description"], {
        "title": idea["title"],
        "style": idea["style"],
        "quelle": idea["source"]
    })
