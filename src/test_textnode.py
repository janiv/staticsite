import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
