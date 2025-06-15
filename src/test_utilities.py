import unittest
from utilities import split_nodes_delimiter
from textnode import TextNode, TextType

class TestUtilities(unittest.TestCase):
    def test_split_nodes_no_delimiter(self):
        nodes = [TextNode("no special formatting", TextType.TEXT)]
        result = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(result, nodes)
        
    def test_split_nodes_delimiter(self):
        nodes = [
            TextNode(text="this a text node with a `code block` text", text_type=TextType.TEXT),
            TextNode(text="this a text node with another `code block` text", text_type=TextType.TEXT),
        ]
        correctnewnodes = [
            TextNode(text="this a text node with a ", text_type=TextType.TEXT),
            TextNode(text="code block", text_type=TextType.CODE),
            TextNode(text=" text", text_type=TextType.TEXT),
            TextNode(text="this a text node with another ", text_type=TextType.TEXT),
            TextNode(text="code block", text_type=TextType.CODE),
            TextNode(text=" text", text_type=TextType.TEXT),
        ]
        newnodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(correctnewnodes, newnodes)
        
    def test_split_nodes_multiple_delimiters(self):
        nodes = [
            TextNode(text="**bold** and _italic_ text", text_type=TextType.TEXT),
        ]
        # First split for bold
        nodes_after_bold = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        # Then split for italic
        nodes_after_italic = split_nodes_delimiter(nodes_after_bold, "_", TextType.ITALIC)
        correct_nodes = [
            TextNode(text="", text_type=TextType.TEXT),
            TextNode(text="bold", text_type=TextType.BOLD),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(text="italic", text_type=TextType.ITALIC),
            TextNode(text=" text", text_type=TextType.TEXT),
        ]
        self.assertEqual(nodes_after_italic, correct_nodes)

    # def test_split_nodes_image_delimiter(self):
    #     nodes = [
    #         TextNode(text="This is an ![image](url) example", text_type=TextType.TEXT),
    #     ]
    #     # Delimiter for images: "![", "]"
    #     nodes_after_image = split_nodes_delimiter(nodes, "![", TextType.IMAGE)
    #     # Should not split as closing delimiter is not handled by split_nodes_delimiter
    #     self.assertEqual(nodes_after_image, [
    #         TextNode(text="This is an ![image](url) example", text_type=TextType.TEXT),
    #     ])

    # def test_split_nodes_link_delimiter(self):
    #     nodes = [
    #         TextNode(text="This is a [link](url) example", text_type=TextType.TEXT),
    #     ]
    #     # Delimiter for links: "[", "]"
    #     nodes_after_link = split_nodes_delimiter(nodes, "[", TextType.LINK)
    #     # Should not split as closing delimiter is not handled by split_nodes_delimiter
    #     self.assertEqual(nodes_after_link, [
    #         TextNode(text="This is a [link](url) example", text_type=TextType.TEXT),
    #     ])

    def test_split_nodes_unclosed_delimiter_raises(self):
        nodes = [
            TextNode(text="This is `unclosed code", text_type=TextType.TEXT),
        ]
        with self.assertRaises(ValueError):
            split_nodes_delimiter(nodes, "`", TextType.CODE)

    def test_split_nodes_multiple_code_blocks(self):
        nodes = [
            TextNode(text="`code1` and `code2`", text_type=TextType.TEXT),
        ]
        correct_nodes = [
            TextNode(text="", text_type=TextType.TEXT),
            TextNode(text="code1", text_type=TextType.CODE),
            TextNode(text=" and ", text_type=TextType.TEXT),
            TextNode(text="code2", text_type=TextType.CODE),
            TextNode(text="", text_type=TextType.TEXT),
        ]
        newnodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        self.assertEqual(newnodes, correct_nodes)

    def test_split_nodes_non_text_type(self):
        nodes = [
            TextNode(text="already bold", text_type=TextType.BOLD),
        ]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, nodes)
if __name__ == '__main__':
    unittest.main()