from enum import Enum
from leafnode import *
from extract import *

class TextType(Enum):
    NORMAL = "normal"
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if self.text != other.text:
            return False
        if self.text_type.value != other.text_type.value:
            return False
        if self.url != other.url:
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match (text_node.text_type):
        case TextType.TEXT:
            return LeafNode(tag=None, value=text_node.text, props=None)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text, props=None)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text, props=None)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text, props=None)
        case TextType.LINK:
            return LeafNode(tag="a", value=text_node.text, props= {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag="img", value=None, props={"src":text_node.url, "alt":text_node.text})
        case __:
            raise Exception("Incompatible text type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            temp_text = node.text.split(delimiter)
            if (len(temp_text) <= 1):
                new_nodes.append(node)
                continue
            for i in range(0, len(temp_text)):
                if not temp_text[i]:
                    continue
                if temp_text[i][-1] != " " and temp_text[i][0] != " ":
                    temp_node = TextNode(text=temp_text[i], text_type=text_type, url=None)
                else:
                    temp_node = TextNode(text=temp_text[i], text_type=TextType.TEXT, url=None)
                new_nodes.append(temp_node)
    return new_nodes


def split_nodes_image(nodes):
    res = []
    for node in nodes:
        txt = node.text
        alts_n_urls = extract_markdown_images(txt)
        if len(alts_n_urls) < 1:
            res.append(node)
            continue
        image_alt = alts_n_urls[0][0]
        image_url = alts_n_urls[0][1]
        sections = txt.split(f"![{image_alt}]({image_url})", 1)
        if len(sections[0]) > 0:
            res.append(TextNode(sections[0], TextType.TEXT))
        res.append(TextNode(image_alt, TextType.IMAGE, image_url))
        if len(sections[1]) > 0:
            extra_node = TextNode(sections[1], TextType.TEXT)
            extra_res = split_nodes_image([extra_node])
            res = res + extra_res
            
    return res

def split_nodes_link(nodes):
    res = []
    for node in nodes:
        txt = node.text
        alts_n_urls = extract_markdown_links(txt)
        if len(alts_n_urls) < 1:
            res.append(node)
            continue
        link_text = alts_n_urls[0][0]
        url = alts_n_urls[0][1]
        sections = txt.split(f"[{link_text}]({url})", 1)
        if len(sections[0]) > 0:
            res.append(TextNode(sections[0], TextType.TEXT))
        res.append(TextNode(link_text, TextType.LINK, url))
        if len(sections[1]) > 0:
            extra_node = TextNode(sections[1], TextType.TEXT)
            extra_res = split_nodes_link([extra_node])
            res = res + extra_res

    return res


def text_to_textnodes(text):
    res = []
    currNode = TextNode(text, TextType.TEXT)
    ttypes = [('`', TextType.CODE), ("**", TextType.BOLD), ("*", TextType.ITALIC)]
    res.append(currNode)
    res = split_nodes_image(res)
    res = split_nodes_link(res)
    for pair in ttypes:
        res = split_nodes_delimiter(res, pair[0], pair[1])
    return res
