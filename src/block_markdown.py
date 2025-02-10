def markdown_to_blocks(markdown):
    unfiltered_blocks =  markdown.split('\n\n')
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