import unittest
from src.gemini_api import setup_gemini, ask_gemini

class TestGeminiAPI(unittest.TestCase):

    def setUp(self):
        self.model = setup_gemini()

    def test_ask_gemini_valid_prompt(self):
        prompt = "What is the capital of France?"
        response = ask_gemini(self.model, prompt)
        self.assertIn("Paris", response)

    def test_ask_gemini_empty_prompt(self):
        prompt = ""
        response = ask_gemini(self.model, prompt)
        self.assertEqual(response, "Hata oluştu: Prompt boş olamaz.")

    def test_ask_gemini_invalid_prompt(self):
        prompt = "Invalid prompt that should trigger an error"
        response = ask_gemini(self.model, prompt)
        self.assertNotIn("Hata oluştu:", response)

if __name__ == "__main__":
    unittest.main()