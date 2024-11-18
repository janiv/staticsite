import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode("h1", "hello")
        node2 = "HTMLNode(h1, hello, None, None)"
        self.assertEqual(node.__repr__, node2)

    def test_repr_2(self):
        node = HTMLNode("h1", "hello", None, {"href":"www.google.com"})
        node2 = HTMLNode("h1", "hello", None, {"href":"www.google.com"})
        self.assertEqual(node.__repr__, node2.__repr__)

    def test_to_html(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html())


if __name__ == "__main__":
    unittest.main()
