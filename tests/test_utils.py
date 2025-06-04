import unittest
from src.utils import load_knowledge_document, save_knowledge_document

class TestUtils(unittest.TestCase):

    def test_load_knowledge_document(self):
        # Test loading a valid knowledge document
        content = load_knowledge_document('knowledge/documents/sample.txt')
        self.assertIsInstance(content, str)
        self.assertGreater(len(content), 0)

    def test_save_knowledge_document(self):
        # Test saving a knowledge document
        test_content = "This is a test knowledge document."
        save_knowledge_document('knowledge/documents/test_doc.txt', test_content)
        
        # Verify the document was saved correctly
        with open('knowledge/documents/test_doc.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, test_content)

    def tearDown(self):
        # Clean up any test documents created
        try:
            os.remove('knowledge/documents/test_doc.txt')
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()