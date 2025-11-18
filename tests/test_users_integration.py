from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user_success():
    payload = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    }
    response = client.post("/users/", json=payload)
    print("\nRESPONSE JSON:", response.json())
    assert response.status_code == 200 or response.status_code == 201

def test_duplicate_email():
    payload = {
        "username": "another",
        "email": "test@example.com",
        "password": "password123"
    }
    response = client.post("/users/", json=payload)
    assert response.status_code == 400
