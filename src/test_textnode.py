import unittest

from textnode import *
from leafnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("A test", TextType.BOLD, "www.someurl.com")
        node2 = TextNode("A test", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_diff_text_types(self):
        node = TextNode("A test", TextType.ITALIC, "www.someurl.com")
        node2 = TextNode("A test", TextType.BOLD, "www.someurl.com")
        self.assertNotEqual(node, node2)

    def test_diff_text(self):
        node = TextNode("A test", TextType.IMAGE, "www.meta.com")
        node2 = TextNode("B test", TextType.IMAGE, "www.meta.com")
        self.assertNotEqual(node, node2)

    def test_textnode_to_htmlnode_bold(self):
        node_b = TextNode("This is bold text", TextType.BOLD, None)
        leaf_node = text_node_to_html_node(node_b)
        self.assertEqual(f"HTMLNode Object (b, {node_b.text}, None, None)", repr(leaf_node))

    def test_textnode_to_html_img(self):
        node = TextNode("This is wrong", TextType.IMAGE, "www.someurl.com")
        leafnode = text_node_to_html_node(node)
        leafnode2 = LeafNode(tag="img", value=None, props={"src":"www.someurl.com", "alt":"This is wrong"})
        self.assertEqual(repr(leafnode), repr(leafnode2))

    def test_textnode_to_html_link(self):
        node = TextNode("This is a link", TextType.LINK, "www.testurl.com")
        leafnode = text_node_to_html_node(node)
        leafnode2 = LeafNode(tag="a", value=node.text, props={"href":node.url})
        self.assertEqual(repr(leafnode), repr(leafnode2))

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        res_arr = [
             TextNode("This is text with a ", TextType.TEXT),
             TextNode("code block", TextType.CODE),
             TextNode(" word", TextType.TEXT),
             ]
        self.assertEqual(new_nodes, res_arr)

    def test_split_nodes_delimiter2(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        res_arr = [
             TextNode("This is text with a ", TextType.TEXT),
             TextNode("bolded", TextType.BOLD),
             TextNode(" word", TextType.TEXT),
             ]
        self.assertEqual(new_nodes, res_arr)

    def test_split_nodes_delimiter3(self):
        node = TextNode("This is text with a **bolded**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        res_arr = [
             TextNode("This is text with a ", TextType.TEXT),
             TextNode("bolded", TextType.BOLD),
             ]
        self.assertEqual(new_nodes, res_arr)

    def test_split_nodes_delimiter4(self):
        node = TextNode("This is text with a **bolded** and *italic* word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        res_arr = [
             TextNode("This is text with a ", TextType.TEXT),
             TextNode("bolded", TextType.BOLD),
             TextNode(" and *italic* word", TextType.TEXT)
             ]
        self.assertEqual(new_nodes, res_arr)


    def test_split_link_node(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
            )
        ans = split_nodes_link([node])
        res_arr = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev")
        ]
        self.assertEqual(ans, res_arr)

    def test_split_image_node(self):
        node = TextNode(
            "This is text with an image link ![pikachu](https://www.serebii.net/pikachu) also foxes are cool!", TextType.TEXT,
            )
        ans = split_nodes_image([node])
        res_arr = [
            TextNode("This is text with an image link ", TextType.TEXT),
            TextNode("pikachu", TextType.IMAGE, "https://www.serebii.net/pikachu"),
            TextNode(" also foxes are cool!", TextType.TEXT)
        ]
        self.assertEqual(ans, res_arr)
        


if __name__ == "__main__":
    unittest.main()
