from textnode import TextNode, TextType
from copy_private_to_public import delete_public, copy_static_to_public
from block_markdown import markdown_to_blocks

def main():
    # delete_public()
    # copy_static_to_public()  
    h1_header = extract_title(get_file_contents("index.md"))
    print(h1_header)
    
    
def extract_title(markdown):    
    h1_header = ''.join(filter(lambda block: block.startswith("# "), markdown_to_blocks(markdown)))
    if not h1_header:
        raise Exception("h1 header not found")
    return h1_header.split(maxsplit=1)[1]
    

def get_file_contents(path):
    with open(path) as file:
        return file.read()


main()