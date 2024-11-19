from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Missing tag")
        if not self.children:
            raise ValueError("Missing children")
        res = ""
        for child in self.children:
            res = res + child.to_html()
        return f"<{self.tag}>" + res + f"</{self.tag}>"
