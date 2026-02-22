import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_none(self):
        tester1 = TextNode("This is a text node", TextType.LINK, "github.com")
        self.assertIsNotNone(tester1)

    def test_not_none(self):
        tester2 = TextNode("This is a text node", TextType.LINK, url = None)
        self.assertIsNone(tester2)

if __name__ == "__main__":
    unittest.main()