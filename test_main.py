from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Weather API is running 🚀"}

def test_weather():
    response = client.get("/weather/Lahore")
    assert response.status_code == 200
    assert "city" in response.json()
