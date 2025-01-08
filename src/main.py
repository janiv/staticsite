from textnode import *
import os
import shutil

def main():
    cwd = os.path.dirname(os.getcwd())
    source = os.path.join(cwd, "static")
    dest = os.path.join(cwd, "public")
    content_mover(source, dest, 0)


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
    
def delete_dest(destination):
    shutil.rmtree(destination)

if __name__ == "__main__":
    main()