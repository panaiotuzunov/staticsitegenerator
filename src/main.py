from textnode import TextNode, TextType
from htmlnode import ParentNode, LeafNode, HTMLNode


def main():
    Test = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(Test)

    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])

    print(parent_node.to_html())

main()

