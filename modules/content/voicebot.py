```python
# modules/content/voicebot.py

import elevenlabs
import whisper
import openai

class VoiceBot:
    def __init__(self, elevenlabs_api_key, whisper_api_key, gpt4o_api_key):
        """Initialize the VoiceBot with API keys."""
        self.elevenlabs_api_key = elevenlabs_api_key
        self.whisper_api_key = whisper_api_key
        self.gpt4o_api_key = gpt4o_api_key
        
        # Initialize API clients
        self.elevenlabs_client = elevenlabs.Client(api_key=self.elevenlabs_api_key)
        self.whisper_client = whisper.Client(api_key=self.whisper_api_key)
        self.gpt4o_client = openai.Client(api_key=self.gpt4o_api_key)
        
    def text_to_speech(self, text, voice='default'):
        """Convert text to speech using ElevenLabs service."""
        try:
            audio = self.elevenlabs_client.text_to_speech(text=text, voice=voice)
            return audio
        except Exception as e:
            print(f"Error in text_to_speech: {e}")
            return None
        
    def transcribe_audio(self, audio_file_path):
        """Transcribe audio file to text using Whisper service."""
        try:
            transcription = self.whisper_client.transcribe(audio_file_path)
            return transcription['text']
        except Exception as e:
            print(f"Error in transcribe_audio: {e}")
            return None

    def get_ai_dialogue(self, prompt, max_tokens=100):
        """Generate AI-based dialogue response using GPT-4o."""
        try:
            response = self.gpt4o_client.completions.create(prompt=prompt, max_tokens=max_tokens)
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error in get_ai_dialogue: {e}")
            return None
```