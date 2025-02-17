from shutil import rmtree, copy
from os import path, listdir, mkdir

def delete_public():
    if path.exists("public/"):  # works only when run from project root                           
        rmtree("public/")       # deletes the folder public and all content
        mkdir("public/")        # creates a new public folder
        print("Succesfully deleted contents of public folder")
    else:
        raise Exception("public folder doesn't exist")

def copy_static_to_public(current_path="static/", dest_path="public/"):
    if path.exists(current_path):
        for item in listdir(current_path):
            source_file = path.join(current_path, item)
            dest_file = path.join(dest_path, item)
            if path.isfile(source_file):
                copy(source_file, dest_file)
                continue
            mkdir(dest_file)
            copy_static_to_public(source_file, dest_file)