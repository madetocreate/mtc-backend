import pytest
from fastapi.testclient import TestClient
from main import app
client = TestClient(app)
def test_health():
    response = client.get("/api/v1/health/")
    assert response.status_code == 200
