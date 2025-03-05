import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_add(client):
    response = client.get('/add?num1=1&num2=20')
    assert response.status_code == 200
    assert response.json['result'] == 30

def test_invalid_input(client):
    response = client.get('/add?num1=abc&num2=20')
    assert response.status_code == 400
    assert "error" in response.json
