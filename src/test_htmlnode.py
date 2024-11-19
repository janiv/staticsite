import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("h1", "hello")
        node2 = "HTMLNode Object (h1, hello, None, None)"
        self.assertEqual(repr(node), node2)

    def test_repr_2(self):
        node = HTMLNode("h1", "hello", None, {"href":"www.google.com"})
        node2 = HTMLNode("h1", "hello", None, {"href":"www.google.com"})
        self.assertEqual(repr(node), repr(node2))

    def test_to_html(self):
        node = HTMLNode("h1", "hello")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        props = {
            "href" : "https://www.google.com",
            "target": "_blank",
        }
        node = HTMLNode("h1", "hello", None, props)
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"", node.props_to_html())


if __name__ == "__main__":
    unittest.main()
