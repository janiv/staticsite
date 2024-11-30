import unittest

from extract import *

class TestExtract(unittest.TestCase):
    def test_extract_markdown_images_1(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text), result)

    def test_extract_markdown_images_5(self):
        text = """This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)
        it also has ![drumroll](https://youtube.com/drumroll) and ![reddit_logo](https://reddit.com/logo)."""
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
                  ("drumroll", "https://youtube.com/drumroll"), ("reddit_logo", "https://reddit.com/logo")]
        self.assertEqual(extract_markdown_images(text), result)

    def test_extract_markdown_images_2(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        result = [("rick roll", "https://i.imgur.com/aKaOqIh.gif")]
        self.assertEqual(extract_markdown_images(text), result)

    def test_extract_markdown_images_3(self):
        text = "This is a text with nothing to find"
        result = []
        self.assertEqual(extract_markdown_images(text), result)
    
    def test_extract_markdown_images_4(self):
        text = "This is a text with ![something] but no url"
        result = []
        self.assertEqual(extract_markdown_images(text), result)
    
    def test_extract_markdown_links_1(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        result =[("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), result)