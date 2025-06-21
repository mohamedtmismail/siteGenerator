from enum import Enum
class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    match block[0]:
        case "#":
            return BlockType.HEADING
        case "`":
            if block[1] == "`" and block[2] == "`":
                return BlockType.CODE
        case ">":
            return BlockType.QUOTE
        case "-":
            return BlockType.UNORDERED_LIST
        case "*":
            return BlockType.UNORDERED_LIST
        case "+":
            return BlockType.UNORDERED_LIST
        case "1":
            if block[:2].isdigit() and block[2] == ".":
                return BlockType.ORDERED_LIST
            elif block[0].isdigit() and block[1] == ".":
                return BlockType.ORDERED_LIST
            else:
                return BlockType.PARAGRAPH
        case _:
            return BlockType.PARAGRAPH