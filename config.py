from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")
ELEVENLABS_KEY = os.getenv("ELEVENLABS_KEY")
ARGIL_KEY = os.getenv("ARGIL_KEY")
