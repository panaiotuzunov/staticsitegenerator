from copy_private_to_public import delete_public, copy_static_to_public
from generate_content import generate_pages_recursive


def main():
    delete_public()
    copy_static_to_public()  
    generate_pages_recursive("content/", "template.html", "public/")


main()