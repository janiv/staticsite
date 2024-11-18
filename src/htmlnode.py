class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        res = ''
        for k,v in self.props.items():
            res = res + f" {k}:\"{v}\""
        return res

    def __repr__(self):
        return f"HTMLNode Object ({self.tag}, {self.value}, {self.children}, {self.props})"
