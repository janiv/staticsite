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


    def test_block_to_block_type(self):
        text = "# This is a heading"
        res = "heading"
        ans = block_to_block_type(text)
        self.assertEqual(res, ans)
    
    
    def test_block_to_block_type2(self):
        text = "#This is a heading"
        res = "normal"
        ans = block_to_block_type(text)
        self.assertEqual(res, ans)
    
    
    def test_block_to_block_type3(self):
        text = "1. This is an ordered list \n2. With at least 2 items\n3. Now three"
        res = "ordered list"
        ans = block_to_block_type(text)
        self.assertEqual(res, ans)

    def test_block_to_block_type4(self):
        text = "- An unordered list\n- Looks weird\n- In this test"
        res = "unordered list"
        ans = block_to_block_type(text)
        self.assertEqual(res, ans)

    def test_block_to_block_quote(self):
        text = ">Just a quote block\n>Lets hope this works\n>Yet again"
        res = "quote"
        ans = block_to_block_type(text)
        self.assertEqual(res, ans)

    def test_block_to_block_botched_quote(self):
        text = ">Just a quote block\n<Lets hope this works\n>Yet again"
        res = "normal"
        ans = block_to_block_type(text)
        self.assertEqual(res, ans)
