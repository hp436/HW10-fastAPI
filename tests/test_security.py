from app.security import hash_password, verify_password

def test_hash_and_verify_password():
    raw = "mypassword123"
    hashed = hash_password(raw)

    assert hashed != raw
    assert verify_password(raw, hashed) is True
    assert verify_password("wrongpass", hashed) is False
