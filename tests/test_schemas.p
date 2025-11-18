import pytest
from pydantic import ValidationError
from app.schemas import UserCreate

def test_valid_user_schema():
    user = UserCreate(username="john", email="john@example.com", password="secret123")
    assert user.username == "john"

def test_invalid_email():
    with pytest.raises(ValidationError):
        UserCreate(username="john", email="invalid-email", password="secret123")
