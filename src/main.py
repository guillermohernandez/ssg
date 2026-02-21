from textnode import TextNode
from textnode import TextType

def main():
    print("hello world")
    new_text = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(new_text)







main()