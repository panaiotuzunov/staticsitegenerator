import re
from textnode import TextType,TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise Exception("Invalid markdown syntax")
        for index in range(len(sections)):
            if not sections[index]:
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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue
        current_text = node.text
        for text, url in images:
            parts = current_text.split(f"![{text}]({url})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.IMAGE, url))
            current_text = parts[1]
        if parts[1]:
            new_nodes.append(TextNode(parts[1], TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links:
            new_nodes.append(node)
            continue
        current_text = node.text
        for text, url in links:
            parts = current_text.split(f"[{text}]({url})", 1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if parts[0]:
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(text, TextType.LINK, url))
            current_text = parts[1]
        if parts[1]:
            new_nodes.append(TextNode(parts[1], TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    text_as_node = TextNode(text, TextType.TEXT)
    return split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(
        split_nodes_delimiter(split_nodes_link(
            split_nodes_image([text_as_node])), '**', TextType.BOLD), '*', TextType.ITALIC), '`', TextType.CODE), '_', TextType.ITALIC)
    

def main():
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    print(text_to_textnodes(text))

main()