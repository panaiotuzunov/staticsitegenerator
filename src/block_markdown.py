from htmlnode import LeafNode, ParentNode

def markdown_to_blocks(markdown):
    unfiltered_blocks = markdown.split('\n\n')
    filtered_blocks = []
    for block in unfiltered_blocks:
        if not block.strip():
            continue
        filtered_blocks.append(block.strip())
    return filtered_blocks


def is_heading(block):
    block_start = block.split(maxsplit = 1)[0]
    match block_start:
        case "#":
            return True
        case "##":
            return True
        case "###":
            return True
        case "####":
            return True
        case "#####":
            return True
        case "######":
            return True
        case _:
            return False


def is_code(block):
    return block.startswith("```") and block.endswith("```")


def is_quote(block):
    lines = block.split('\n')
    for line in lines:
        if line and line[0] != '>':
            return False
    return True 


def is_unordered_list(block):
    lines = block.split('\n')
    for line in lines:
        line_start = line.split(maxsplit = 1)[0]
        if line_start != '*' and line_start != '-':
            return False
    return True


def is_ordered_list(block):
    lines = block.split('\n')
    for num, line in enumerate(lines, 1):
        line_start = line.split(maxsplit = 1)[0]
        if line_start != f"{num}.":
            return False
    return True


def block_to_block_type(block):
    if is_heading(block):
        return "heading"
    if is_code(block):
        return "code"
    if is_quote(block):
        return "quote"
    if is_unordered_list(block):
        return "unordered_list"
    if is_ordered_list(block):
        return "ordered_list"
    return "paragraph"


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes_lst = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case "heading":
                tag = f"h{len(block.split(maxsplit = 1)[0])}"
                value = block.split(maxsplit = 1)[1]
                nodes_lst.append(LeafNode(tag, value))
            case "code":
                first_tag = "pre"
                second_tag = "code"
                value = block[3:-3]
                nodes_lst.append(ParentNode(first_tag, [LeafNode(second_tag, value)]))
            case "quote":          # TODO add support for <cite> as a prop
                tag = "blockquote"
                value = block[1:-1]
                nodes_lst.append(LeafNode(tag, value))
            case "unordered_list":
                tag = "ul"
                nodes_lst.append(list_elements_to_html_node(tag, block))
            case "ordered_list":
                tag = "ol"
                nodes_lst.append(list_elements_to_html_node(tag, block))
            case "paragraph":
                tag = "p"
                nodes_lst.append(LeafNode(tag, block))
            case _:
                raise ValueError("Block type not found") #Should never be raised, added just in case. Get it... in case... LOL
    return ParentNode("div", nodes_lst) 


def list_elements_to_html_node(tag, block):
    lines = block.split('\n')
    nodes = []
    start = 2
    if tag == "ol":
        start = 3
    for line in lines:
        nodes.append(LeafNode("li", line[start:]))
    return ParentNode(tag, nodes)