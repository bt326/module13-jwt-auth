import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_success():
    unique = str(uuid.uuid4())[:8]

    response = client.post(
        "/users",
        json={
            "username": f"user_{unique}",
            "email": f"{unique}@test.com",
            "password": "123456"
        }
    )
    assert response.status_code == 200

def test_invalid_email():
    response = client.post(
        "/users",
        json={
            "username": "user_invalid",
            "email": "wrong-email",
            "password": "123456"
        }
    )
    assert response.status_code == 400

def test_duplicate_user():
    unique = str(uuid.uuid4())[:8]
    username = f"user_{unique}"
    email = f"{unique}@test.com"

    client.post(
        "/users",
        json={
            "username": username,
            "email": email,
            "password": "123456"
        }
    )

    response = client.post(
        "/users",
        json={
            "username": username,
            "email": email,
            "password": "123456"
        }
    )

    assert response.status_code == 400