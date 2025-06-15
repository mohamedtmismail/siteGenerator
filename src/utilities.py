from textnode import TextType,TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            nodesfound = node.text.split(delimiter)
            if len(nodesfound) %2 == 0:
                raise ValueError("no closing delimiter was found")
            
            for i in range(len(nodesfound)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(text = nodesfound[i], text_type = TextType.TEXT))
                else:
                    new_nodes.append(TextNode(text=nodesfound[i], text_type=text_type))
    return new_nodes