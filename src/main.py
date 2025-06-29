from textnode import TextNode
from textnode import TextType
import os
import shutil

def main():
    testnode = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.bootdev"
    )
    print(testnode)
    copy_tree("./static", "./public")
    
def copy_tree(source_dir, dest_dir):
    # if destination directory exists delete it
    if os.path.exists(dest_dir):
        print(f"Found {dest_dir} directory. Now deleting...")
        shutil.rmtree(dest_dir)
        print(f"{dest_dir} directory cleared")
    
    os.mkdir(dest_dir)
    if os.path.exists(source_dir):
        for item in os.listdir(source_dir):
            item_source_path = os.path.join(source_dir,item)
            item_dest_path = os.path.join(dest_dir,item)
            if os.path.isfile(item_source_path):
                print(f"copying {item_source_path} --> {item_dest_path}")
                shutil.copy(item_source_path, item_dest_path)
            else:
                print(f"copying files in dir:{item_source_path} --> {item_dest_path}")
                copy_tree(item_source_path, item_dest_path)
        
if __name__ == "__main__":
    main()
