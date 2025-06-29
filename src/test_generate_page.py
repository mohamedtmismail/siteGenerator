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
        
    def test_extract_title_multiple_headings(self):
        md = """# Heading1
## h2
### h3
#### h4"""
        title = extract_title(md)
        self.assertEqual(
            "Heading1",
            title
        )
        
    def test_extract_title_no_h1(self):
        md = "Hi mom"
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "no title found")
        
if __name__ == "__main__":
    unittest.main()