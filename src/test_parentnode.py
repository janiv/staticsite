import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", node.to_html())

    def test_to_html_nested(self):

        nodesList = [
            LeafNode("b", "Bold text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Some text"),
        ]
        nodesList2 = [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            
        ]
        node = ParentNode(
            "div",
            [   
            ParentNode("p", nodesList),
            ParentNode("p", nodesList2)
            ],
        )
        self.assertEqual("<div><p><b>Bold text</b><i>Italic text</i>Some text</p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>", node.to_html())

    def test_missing_tag(self):
        node = ParentNode(
            None,
            [   
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
            ],
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_missing_children(self):
        node = ParentNode(
            "p",
            []
        )
        with self.assertRaises(ValueError):
            node.to_html()