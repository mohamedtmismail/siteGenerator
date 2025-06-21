import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
        
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdown_images_double(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"),("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
        
    def test_extract_markdownlink_links(self):
        matches = extract_markdown_links(
            "this is text with a [link](https://www.google.com)"
        )
        self.assertListEqual([("link","https://www.google.com")], matches)
        
    def test_extract_markdownlink_links_double(self):
        matches = extract_markdown_links(
            "this is text with a [link](https://www.google.com), and another [link](https://www.facebook.com)"
        )
        self.assertListEqual([("link","https://www.google.com"), ("link","https://www.facebook.com")], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        
        new_nodes = split_nodes_image([node])
        
        testnodes = [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        
        self.assertListEqual(testnodes,new_nodes,)
        
    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        
        testnodes = [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        
        self.assertListEqual(testnodes,new_nodes,)
    
    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )
        
    def test_text_to_textnodes(self):
        new_nodes = text_to_textnodes(
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
            
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                ],
            new_nodes
            )
    def test_text_to_textnodes_only_text(self):
        new_nodes = text_to_textnodes("Just plain text with no formatting.")
        self.assertListEqual(
            [TextNode("Just plain text with no formatting.", TextType.TEXT)],
            new_nodes
        )

    def test_text_to_textnodes_only_bold(self):
        new_nodes = text_to_textnodes("**bold**")
        self.assertListEqual(
            [TextNode("bold", TextType.BOLD)],
            new_nodes
        )

    def test_text_to_textnodes_only_italic(self):
        new_nodes = text_to_textnodes("_italic_")
        self.assertListEqual(
            [TextNode("italic", TextType.ITALIC)],
            new_nodes
        )

    def test_text_to_textnodes_only_code(self):
        new_nodes = text_to_textnodes("`code`")
        self.assertListEqual(
            [TextNode("code", TextType.CODE)],
            new_nodes
        )

    def test_text_to_textnodes_only_image(self):
        new_nodes = text_to_textnodes("![alt](url)")
        self.assertListEqual(
            [TextNode("alt", TextType.IMAGE, "url")],
            new_nodes
        )

    def test_text_to_textnodes_only_link(self):
        new_nodes = text_to_textnodes("[desc](url)")
        self.assertListEqual(
            [TextNode("desc", TextType.LINK, "url")],
            new_nodes
        )

    def test_text_to_textnodes_mixed_adjacent(self):
        new_nodes = text_to_textnodes("**bold**_italic_`code`")
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode("italic", TextType.ITALIC),
                TextNode("code", TextType.CODE),
            ],
            new_nodes
        )

    def test_text_to_textnodes_nested_like(self):
        # Not true nesting, but adjacent formatting
        new_nodes = text_to_textnodes("**bold _italic_**")
        self.assertListEqual(
            [
                TextNode("bold _italic_", TextType.BOLD),
            ],
            new_nodes
        )

    def test_text_to_textnodes_multiple_images_and_links(self):
        new_nodes = text_to_textnodes(
            "![img1](url1) and [link1](url2) and ![img2](url3) and [link2](url4)"
        )
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "url1"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link1", TextType.LINK, "url2"),
                TextNode(" and ", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "url3"),
                TextNode(" and ", TextType.TEXT),
                TextNode("link2", TextType.LINK, "url4"),
            ],
            new_nodes
        )

    def test_text_to_textnodes_text_before_and_after_formatting(self):
        new_nodes = text_to_textnodes("Start **bold** end")
        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" end", TextType.TEXT),
            ],
            new_nodes
        )
        

    def test_text_to_textnodes_empty_string(self):
        new_nodes = text_to_textnodes("")
        self.assertListEqual(
            [],
            new_nodes
        )
if __name__ == "__main__":
    unittest.main()
