import unittest

from blocks import *


class TestBlocks(unittest.TestCase):
    def test_blocks_1(self):
        text  = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        res = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            """* This is the first list item in a list block
* This is a list item
* This is another list item"""
        ]
        ans = markdown_to_blocks(text)
        self.assertEqual(res, ans)

    def test_blocks_2(self):
        text = "#This is a heading"
        res = ["#This is a heading"]
        ans = markdown_to_blocks(text)
        self.assertEqual(res, ans)