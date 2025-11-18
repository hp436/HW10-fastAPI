import os

# Import database path from your application
from app.database import DB_PATH

# -------- IMPORTANT TEST FIX --------
# Delete the existing database before tests run
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
# ------------------------------------

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
    body = response.json()
    assert body["username"] == "testuser"
    assert body["email"] == "test@example.com"


def test_duplicate_email():
    payload = {
        "username": "testuser2",
        "email": "test@example.com",
        "password": "anotherpass"
    }

    response = client.post("/users/", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"
