from htmlnode import *
from blocks import *
from textnode import *
from parentnode import *

def markdown_to_html_node(markdown):
    parent = ParentNode(tag="div", children=None, props = None)
    html_children = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == "heading":
            pound_count = count_pounds(block)
            h_type = heading_type(pound_count)
            h_val = strip_pounds(block, pound_count)
            new_node = LeafNode(tag=h_type, value=h_val)
            html_children.append(new_node)
        if block_type == "code":
            code_node = LeafNode(tag="code", value=block, children=None, props=None)
            pre_node = ParentNode(tag="pre" , children=code_node, props=None)
            html_children.append(pre_node)
        if block_type == "quote":
            q_val = strip_quote_block(block)
            quote_node = LeafNode(tag="blockquote", value=q_val)
            html_children.append(quote_node)
        if block_type == "unordered list":
            list_nodes = []
            split_text = block.split('\n')
            split_text = strip_unordered_list(split_text)
            for line in split_text:
                text_nodes=  text_to_textnodes(line)
                kiddos = []
                for tn in text_nodes:
                    leaf = text_node_to_html_node(tn)
                    kiddos.append(leaf)
                node = ParentNode(tag="li", children=kiddos)
                list_nodes.append(node)            
            list_node = ParentNode(tag="ul", children=list_nodes)
            html_children.append(list_node)
        if block_type == "ordered list":
            list_nodes = []
            split_text = block.split('\n')
            split_text = strip_number(split_text)
            for line in split_text:
                text_nodes=  text_to_textnodes(line)
                kiddos = []
                for tn in text_nodes:
                    leaf = text_node_to_html_node(tn)
                    kiddos.append(leaf)
                node = ParentNode(tag="li", children=kiddos)
                list_nodes.append(node)
            list_node = ParentNode(tag="ol", children=list_nodes)
            html_children.append(list_node)
        if block_type == "normal":
            nodes = text_to_children(block)
            p_node = ParentNode(tag="p", children=nodes)
            html_children.append(p_node)
    parent.children=html_children
    return parent

def strip_number(text_as_list):
    res = []
    for line in text_as_list:
        period_and_space = line.find('. ')
        line = line[period_and_space+2:]
        res.append(line)
    return res

def strip_unordered_list(text_as_list):
    res = []
    for line in text_as_list:
        space = line.find(' ')
        line = line[space+1:]
        res.append(line)
    return res


def count_pounds(text):
    headings_pattern = r"^[#]{1,6}[ ][\S]"
    pound_match = re.search(headings_pattern, text)
    if(pound_match):
        match_string = pound_match.group(0)
        match_string = match_string[:-2] #In case we have a header starting with #
        return match_string.count('#')
    else:
        raise ValueError(f"This is supposed to be called on a header not {text}")

def strip_quote_block(text):
    return text[1:].strip()


def strip_pounds(text, count):
    # Count+1 to strip all pounds and leading space
    return text[count+1:]


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
    raise ValueError(f"Your # count of {count} is not acceptable")

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        htmled_node = text_node_to_html_node(node)
        html_nodes.append(htmled_node)
    return html_nodes


