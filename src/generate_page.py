
def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        line = line.strip()
        if line.startswith("# "):
            return line[2:]
    raise Exception("no title found")


    
        