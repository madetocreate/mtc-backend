import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_tts():
    response = client.post("/api/v1/tts/", json={"text": "test"})
    assert response.status_code == 200
