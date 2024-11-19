
import unittest

from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(tag="p", value="This is a test", props=None)
        self.assertEqual("<p>This is a test</p>", node.to_html())

    def test_to_html_with_props(self):
        props = {
            "href" : "https://www.google.com"
        }
        node = LeafNode("a", "Click me!", props)
        self.assertEqual("<a href=\"https://www.google.com\">Click me!</a>", node.to_html())
