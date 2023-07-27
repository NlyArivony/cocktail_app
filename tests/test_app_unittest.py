import unittest
from app import create_app, db


class FlaskAPITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_cocktail(self):
        # Test creating a new cocktail
        data = {
            "name": "Test Cocktail",
            "ingredients": "Ingredient A, Ingredient B",
            "instructions": "Mix everything together.",
        }
        response = self.client.post("/cocktails", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json)

    def test_get_cocktail(self):
        # Test retrieving a cocktail
        data = {
            "name": "Test Cocktail",
            "ingredients": "Ingredient A, Ingredient B",
            "instructions": "Mix everything together.",
        }
        response = self.client.post("/cocktails", json=data)
        self.assertEqual(response.status_code, 201)
        cocktail_id = response.json["id"]

        response = self.client.get(f"/cocktails/{cocktail_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["name"], "Test Cocktail")

    def test_get_all_cocktails(self):
        # Test retrieving all cocktails
        response = self.client.get("/cocktails")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

    def test_delete_cocktail(self):
        # Test deleting a cocktail
        data = {
            "name": "Test Cocktail",
            "ingredients": "Ingredient A, Ingredient B",
            "instructions": "Mix everything together.",
        }
        response = self.client.post("/cocktails", json=data)
        self.assertEqual(response.status_code, 201)
        cocktail_id = response.json["id"]

        response = self.client.delete(f"/cocktails/{cocktail_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json["message"], "Cocktail deleted successfully")

        # Check that the cocktail is no longer available
        response = self.client.get(f"/cocktails/{cocktail_id}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json["message"], "Cocktail not found")


if __name__ == "__main__":
    unittest.main()
