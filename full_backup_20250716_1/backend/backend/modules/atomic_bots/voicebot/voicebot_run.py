from .voice_input import record_voice
from .voice_tts import speak

def run_voicebot():
    prompt = record_voice()
    speak(f"Antwort auf: {prompt}")
