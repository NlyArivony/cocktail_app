import pytest
from app import create_app, db


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

        with app.app_context():
            db.drop_all()


def test_create_cocktail(client):
    # Test creating a new cocktail
    data = {
        "name": "Test Cocktail",
        "ingredients": "Ingredient A, Ingredient B",
        "instructions": "Mix everything together.",
    }
    response = client.post("/cocktails", json=data)
    assert response.status_code == 201
    assert "id" in response.json


def test_get_cocktail(client):
    # Test retrieving a cocktail
    data = {
        "name": "Test Cocktail",
        "ingredients": "Ingredient A, Ingredient B",
        "instructions": "Mix everything together.",
    }
    response = client.post("/cocktails", json=data)
    assert response.status_code == 201
    cocktail_id = response.json["id"]

    response = client.get(f"/cocktails/{cocktail_id}")
    assert response.status_code == 200
    assert response.json["name"] == "Test Cocktail"


def test_get_all_cocktails(client):
    # Test retrieving all cocktails
    response = client.get("/cocktails")
    assert response.status_code == 200
    assert isinstance(response.json, list)


def test_delete_cocktail(client):
    # Test deleting a cocktail
    data = {
        "name": "Test Cocktail",
        "ingredients": "Ingredient A, Ingredient B",
        "instructions": "Mix everything together.",
    }
    response = client.post("/cocktails", json=data)
    assert response.status_code == 201
    cocktail_id = response.json["id"]

    response = client.delete(f"/cocktails/{cocktail_id}")
    assert response.status_code == 200
    assert response.json["message"] == "Cocktail deleted successfully"

    # Check that the cocktail is no longer available
    response = client.get(f"/cocktails/{cocktail_id}")
    assert response.status_code == 404
    assert response.json["message"] == "Cocktail not found"
