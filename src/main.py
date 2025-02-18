from textnode import TextNode, TextType
from copy_private_to_public import delete_public, copy_static_to_public
from block_markdown import markdown_to_blocks, markdown_to_html_node

def main():
    delete_public()
    copy_static_to_public()  
    generate_page("content/index.md", "template.html", "public/index.html")

    
def extract_title(markdown):    
    h1_header = ''.join(filter(lambda block: block.startswith("# "), markdown_to_blocks(markdown)))
    if not h1_header:
        raise Exception("h1 header not found")
    return h1_header.split(maxsplit=1)[1]
    

def get_file_contents(path):
    with open(path) as file:
        return file.read()
    

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    template_file = get_file_contents(template_path)
    source_file = get_file_contents(from_path)
    source_html = markdown_to_html_node(source_file).to_html()
    title = extract_title(source_file)
    new_html = template_file.replace("{{ Title }}", title).replace("{{ Content }}", source_html)
    with open(dest_path, "w") as file:
        file.write(new_html)


main()