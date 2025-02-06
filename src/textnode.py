from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (
            self.text == other.text and 
            self.text_type == other.text_type and 
            self.url == other.url
            )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    def text_node_to_html_node(text_node):
        match text_node.text_type:
            case text_node.text_type.TEXT:
                return
            case text_node.text_type.BOLD:
                return
            case text_node.text_type.ITALIC:
                return
            case text_node.text_type.CODE:
                return
            case text_node.text_type.LINK:
                return
            case text_node.text_type.IMAGE:
                 return
            case _:
                raise Exception("TextType not found")       
