from app.security import hash_password, verify_password

def test_hash_password():
    password = "secret123"
    hashed = hash_password(password)

    assert hashed != password
    assert verify_password(password, hashed) is True

def test_wrong_password():
    password = "secret123"
    hashed = hash_password(password)

    assert verify_password("wrongpass", hashed) is False