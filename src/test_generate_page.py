import unittest
from generate_page import extract_title
class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(
            "Hello",
            title
        )
        

if __name__ == "__main__":
    unittest.main()