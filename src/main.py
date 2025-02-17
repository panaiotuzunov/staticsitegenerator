from textnode import TextNode, TextType
from copy_private_to_public import delete_public, copy_static_to_public


def main():
    delete_public()
    copy_static_to_public()    


main()