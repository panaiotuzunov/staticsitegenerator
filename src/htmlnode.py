class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag              #string
        self.value = value          #string
        self.children = children    #list of HTMLNode objects
        self.props = props          #dictionary / example - {"href": "https://www.google.com"}

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ""
        for key, value in self.props.items():
            result += f' {key}={value}'
        return result
    
    def __repr__(self):
        result = f"tag={self.tag}\n"
        result += f"value={self.value}\n"
        result += f"List of children objects: {self.children}\n"
        result += f"Props key=value:\n"
        result += self.props_to_html()
        return result
       
