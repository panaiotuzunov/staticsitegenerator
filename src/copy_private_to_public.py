from shutil import rmtree, copy
from os import path, listdir, mkdir

def delete_public():
    if path.exists("public/"):  # works only when run from project root                           
        rmtree("public/")       # deletes the folder public and all content
        mkdir("public/")        # creates a new public folder
        print("Succesfully deleted contents of public folder")
    else:
        raise Exception("public folder doesn't exist")

def copy_static_to_public():
    current_path = "static/"
    if path.exists(current_path):
        for item in listdir(current_path):
            if path.isfile(path.join(current_path, item)):
                print(f"file - {item}")
                continue
            print(f"folder - {item}")
            


def main():
    copy_static_to_public()


main()