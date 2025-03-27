from copy_private_to_public import delete_public, copy_static_to_public
from generate_content import generate_pages_recursive
from os import path
import sys


def main():
    basepath = './'
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    content_path = path.join(basepath, "content")
    template_path = path.join(basepath, "template.html")
    public_path = path.join(basepath, "docs")
    static_path = path.join(basepath, "static")
    delete_public(public_path)
    copy_static_to_public(static_path, public_path)  
    generate_pages_recursive(content_path, template_path, public_path, basepath)


main()