from textnode import TextNode
from textnode import TextType


def main():
    testnode = TextNode(
        "This is some anchor text", TextType.LINK, "https://www.bootdev"
    )
    print(testnode)


if __name__ == "__main__":
    main()
