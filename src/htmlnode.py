class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              #string
        self.value = value          #string
        self.children = children    #list of HTMLNode objects
        self.props = props          #dictionary / example - {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        result = ""
        if self.props is None:
            return result
        for key, value in self.props.items():
            result += f' {key}="{value}"'
        return result
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
       

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"