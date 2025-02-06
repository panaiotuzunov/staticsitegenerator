from textnode import TextType,TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:                               #TODO Nesting of inline elements
            split_nodes_text = node.text.split(delimiter, maxsplit=2)
            new_nodes.extend(
                [TextNode(split_nodes_text[0], TextType.TEXT),
                TextNode(split_nodes_text[1], text_type),
                TextNode(split_nodes_text[2], TextType.TEXT)]
            )         
    return new_nodes    