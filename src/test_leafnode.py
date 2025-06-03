import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_a_with_props(self):
       node = LeafNode("a",
                       "press this link",
                       {"class": "greeting",
                        "href": "https://boot.dev"})
       self.assertEqual(node.to_html(),'<a class="greeting" href="https://boot.dev">press this link</a>')
    def test_leaf_to_html_b(self):
        node = LeafNode(
            "b",
            "this is bold text",
        )
        self.assertEqual(node.to_html(), "<b>this is bold text</b>")
        
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
if __name__ == "__main__":
    unittest.main()