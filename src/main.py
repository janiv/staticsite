from textnode import *
from markdownconverter import *
import os
import shutil
import pathlib

def main():
    cwd = os.path.dirname(os.getcwd())
    source = os.path.join(cwd, "staticsite/static")
    print(cwd)
    print(source)
    dest = os.path.join(cwd, "staticsite/public")
    content_mover(source, dest, 0)
    from_path = os.path.join(cwd, "staticsite/content")
    template_path = os.path.join(cwd, "staticsite/template.html")
    generate_page_recursive(from_path, template_path, dest)

def content_mover(source, destination, status):
    #First we delete, I am cheating and using an int
    if status == 0:
        if os.path.exists(destination):
            delete_dest(destination)
        status += 1
        content_mover(source, destination, status)
        return
    #If destination don't exist we need to make it
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        #If we find another directory we need to call content_mover again
        curr = os.path.join(source, item)
        if not os.path.isfile(curr):
            content_mover(curr, os.path.join(destination, item), status)
        else:
            #We found a file, we can copy it to the destination
            shutil.copy(curr, destination) 

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
    markdown_file = open(from_path, "r")
    markdown = markdown_file.read()
    markdown_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    title_string = extract_title(markdown)
    html = markdown_to_html_node(markdown)
    html_string = html.to_html()

    template =template.replace("{{ Title }}", title_string)
    template =template.replace("{{ Content }}", html_string)

    dest_path = os.path.join(dest_path, "index.html")
    destination = open(dest_path, "w")
    destination.write(template)
    destination.close()


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    dir_content = os.listdir(dir_path_content)
    for dc in dir_content:
        dc_val = os.path.join(dir_path_content, dc)
        if os.path.isfile(dc_val):
            generate_page(dc_val, template_path, dest_dir_path)
        else:
            # We have found a folder, we would like to write to public/{found_folder}
            dest = os.path.join(dest_dir_path, dc)
            generate_page_recursive(dc_val, template_path, dest)
            
        


def delete_dest(destination):
    shutil.rmtree(destination)

if __name__ == "__main__":
    main()