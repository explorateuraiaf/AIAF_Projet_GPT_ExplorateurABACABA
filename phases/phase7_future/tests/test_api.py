import unittest
import json
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_ping(self):
        res = self.client.get("/ping")
        self.assertEqual(res.status_code, 200)

    def test_prompt_score(self):
        res = self.client.post("/prompt/score", json={"prompt": "analyse fractale"})
        self.assertEqual(res.status_code, 200)
        self.assertIn("score", res.get_json())

if __name__ == "__main__":
    unittest.main()
