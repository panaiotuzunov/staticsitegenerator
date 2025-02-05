from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode, HTMLNode


def main():
    #Test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    #print(Test)
    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)
    print(node.to_html())



main()

