import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_memory():
    response = client.post("/api/v1/memory/", json={"prompt": "Hello"})
    assert response.status_code == 200
    response = client.get("/api/v1/memory/")
    assert response.status_code == 200
