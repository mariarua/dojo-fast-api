from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_say_hello():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message":"hello world"}

def test_get_user():
    response = client.get("/users/1", headers={"x-token":"fastApiToken"})
    assert response.status_code == 200
    assert response.json() == {
                                "id": 1,
                                "name": "juana",
                                "email": "juana@udea.edu.co",
                                "password": "pass123"
                            }

def test_get_user_bad_token():
    response = client.get("users/1", headers={"x-token":"invalidToken"})
    assert response.status_code == 400
    assert response.json() == {"detail":"Invalid X-Token header"}

def test_create_item():
    newUser = {
                "id": 4,
                "name": "Peter parker",
                "email": "Spydi@dc.com",
                "password": "Avengers 3.0"
            }
    response = client.post("/users", json=newUser)
    assert response.status_code == 200
    assert response.json() == newUser
