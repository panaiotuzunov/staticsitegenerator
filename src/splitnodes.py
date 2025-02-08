import re
from textnode import TextType,TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:                               #TODO Nesting of inline elements
            sections = node.text.split(delimiter)
            if len(sections) % 2 == 0:
                raise Exception("Invalid markdown syntax")
            else:
                for index in range(len(sections)):
                    if sections[index] == "":
                        continue
                    if index % 2 == 0:
                        new_nodes.append(TextNode(sections[index], TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(sections[index], text_type))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)      


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)  