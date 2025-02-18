from block_markdown import markdown_to_blocks, markdown_to_html_node
from os import path, makedirs, listdir

def extract_title(markdown):    
    h1_header = ''.join(filter(lambda block: block.startswith("# "), markdown_to_blocks(markdown)))
    if not h1_header:
        raise Exception("h1 header not found")
    return h1_header[2:]
    

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
    
    dest_dir_path = path.dirname(dest_path)
    if dest_dir_path != "":
        makedirs(dest_dir_path, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(new_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in listdir(dir_path_content):
        current_content = path.join(dir_path_content, item)
        current_dest = path.join(dest_dir_path, item)
        if path.isfile(current_content):
            generate_page(current_content, template_path, path.join(path.dirname(current_dest), "index.html"))
        else:
            generate_pages_recursive(current_content, template_path, current_dest)
    
        