import os
from markdown_blocks import markdown_to_html_node
from pathlib import Path


def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path)
        else:
            generate_page_recursive(from_path,template_path, dest_path)



def generate_page(from_path, template_path, dest_path):
    print(f"Genertating page form {from_path} to {dest_path} using {template_path}")
    
    md = ""
    template_content = ""
    try:
        with open(from_path, 'r') as file:
            md = file.read()
            if md == "": raise Exception(f"file at {from_path} is empty")
    except FileNotFoundError:
        print(f"File:{from_path} not found!")
    except Exception as e:
        print(f"Error reading file: {e}")
        
    try:
        with open(template_path,'r') as file:
            template_content = file.read()
            if template_content == "": raise Exception(f"template file:{template_path} is empty")
    except FileNotFoundError:
        print(f"template not found at {template_path}")
    except Exception as e:
        print(f"Error reading file: {e}")
    
    html = markdown_to_html_node(md).to_html()
    print(html)
    title = extract_title(md)
    print(title)
    page_with_title = template_content.replace("{{ Title }}", title)
    page_with_content = page_with_title.replace("{{ Content }}", html)
    
    parent_dir = os.path.dirname(dest_path)
    if parent_dir: os.makedirs(parent_dir, exist_ok=True)
    
    with open(dest_path, 'w') as file:
        file.write(page_with_content)
    print(f"File created at: {dest_path}")
        
def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise Exception("no title found")
        
        

    
        