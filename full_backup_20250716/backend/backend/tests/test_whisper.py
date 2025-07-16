import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_whisper():
    response = client.post("/api/v1/whisper/", files={"file": ("audio.wav", b"fake-audio", "audio/wav")})
    assert response.status_code == 200
