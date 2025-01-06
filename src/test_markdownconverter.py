import unittest
from markdownconverter import *

class TestMarkDownConverter(unittest.TestCase):
    def test_strip_number(self):
        text = "1. This\n2. Is\n3. A test"
        res = ["This", "Is", "A test"]
        ans = strip_number(text.split('\n'))
        self.assertEqual(res, ans)

    def test_strip_unordered_list(self):
        text = "- This\n- Is\n- A test"
        res = ["This", "Is", "A test"]
        ans = strip_unordered_list(text.split('\n'))
        self.assertEqual(res, ans)

    def test_strip_pounds(self):
        text = "### A header"
        res = "A header"
        ans = strip_pounds(text, 3)
        self.assertEqual(ans, res)

    
    def test_count_pound(self):
        text = "### Four"
        res = 3
        ans = count_pounds(text)
        self.assertEqual(res, ans)
    
    
    def test_count_pound2(self):
        text = "####### Broken"
        with self.assertRaises(ValueError):
            count_pounds(text)