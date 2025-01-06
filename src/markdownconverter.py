from htmlnode import *
from blocks import *
from textnode import *

def markdown_to_html_node(markdown):
    parent = HTMLNode(tag="div", value=None, children=None, props = None)
    html_children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            pound_count = count_pounds(block)
            h_type = heading_type(pound_count)
            new_node = HTMLNode(tag=h_type, value=block)
            html_children.append(new_node)
        if block_type == "code":
            return 2
        if block_type == "quote":
            return 3
        if block_type == "unordered list":
            return 4
        if block_type == "ordered list":
            return 5
        if block_type == "normal":
            return 6


    return parent


def count_pounds(text):
    headings_pattern = r"^[#]{1,6}[ ][\S]"
    pound_match = re.search(headings_pattern, text)
    if(pound_match):
        match_string = pound_match.group(0)
        match_string = match_string[:-2] #In case we have a header starting with #
        return match_string.count('#')
    else:
        raise ValueError(f"This is supposed to be called on a header not {text}")

def heading_type(count):
    if count == 1:
        return "h1"
    if count == 2:
        return "h2"
    if count == 3:
        return "h3"
    if count == 4:
        return "h4"
    if count == 5:
        return "h5"
    if count == 6:
        return "h6"
    raise ValueError(f"Your count of {count} is not acceptable")

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        htmled_node = text_node_to_html_node(node)
        html_nodes.append(htmled_node)
    return html_nodes