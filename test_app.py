from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200


def test_login_with_email():
    response = client.get("/login?email=aditi@example.com")

    assert response.status_code == 200
    assert response.json()["message"] == "Welcome aditi@example.com"