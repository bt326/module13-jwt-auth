from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user_success():
    response = client.post(
        "/users",
        json={
            "username": "user_test_1",
            "email": "user_test_1@test.com",
            "password": "123456"
        }
    )
    assert response.status_code == 200

def test_invalid_email():
    response = client.post(
        "/users",
        json={
            "username": "user_test_2",
            "email": "wrong-email",
            "password": "123456"
        }
    )
    assert response.status_code == 400

def test_duplicate_user():
    client.post(
        "/users",
        json={
            "username": "duplicate1",
            "email": "duplicate1@test.com",
            "password": "123456"
        }
    )

    response = client.post(
        "/users",
        json={
            "username": "duplicate1",
            "email": "duplicate1@test.com",
            "password": "123456"
        }
    )

    assert response.status_code == 400