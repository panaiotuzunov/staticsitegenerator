from copy_private_to_public import delete_public, copy_static_to_public
from generate_content import generate_pages_recursive
from os import path
import sys


static_path = "./static"
public_path = "./docs"
content_path = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:   
        basepath = sys.argv[1]  
    delete_public(public_path)
    copy_static_to_public(static_path, public_path)  
    generate_pages_recursive(content_path, template_path, public_path, basepath)


main()