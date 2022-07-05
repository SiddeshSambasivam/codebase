"""
https://en.wikipedia.org/wiki/Huffman_coding

Given a text, return the Huffman coding table of all the characters (including space if it has).

For example, given "this is an example of a huffman tree", return the table:

111
a 101
e 011
f 1101
h 1000
i 0000
l 00100
m 0101
n 0011
o 00011
p 00101
r 10011
s 1100
t 0100
u 00010
x 10010 

 aefhilmnoprstux

abcdef

# 0 -> left
# 1 -> right       


"""

from collections import Counter
import heapq
from typing import Type
from unittest import result

class TreeNode:
    def __init__(
        self,
        char: str,
        value: int,
        left: "TreeNode" = None,
        right: "TreeNode" = None,
        enc_bit: int = None,
    ):

        self.char = char
        self.value = value
        self.left = left
        self.right = right

        self.enc_bit = enc_bit  # 0/1


    def __lt__(self, obj) -> bool:
        # print('Operator Override',self.value, obj.value)

        return self.value < obj.value

    def __str__(self) -> str:
        return f"TreeNode<Char={self.char} Value={self.value}>"


class HuffmanEncoding:
    def __init__(self, string: str) -> None:

        self.string = string
        self.freq2char = Counter(string)
        self.root = self.create_tree()
        # self.root = self.create_tree_heap()

        self.table = dict()  # char -> bit_value


    def create_tree_heap(self) -> TreeNode:
        """Creates a binary tree with heap implementation"""

        nodes = list()

        for char, freq in self.freq2char.items():
            node = TreeNode(char, freq)
            nodes.append(node)

        heapq.heapify(nodes)

        while len(nodes) >= 2:

            left = heapq.heappop(nodes)
            right = heapq.heappop(nodes)

            parent_node = TreeNode(char="", value=(left.value+right.value), left=left, right=right)

            heapq.heappush(nodes, parent_node)

        return nodes[0]

    def create_tree(self) -> TreeNode:
        """Creates the binary tree for the given nodes of characters"""

        nodes = list()

        for char, freq in self.freq2char.items():
            node = TreeNode(char, freq)
            nodes.append(node)

        sorted_nodes = self.sort(nodes)

        # for node in sorted_nodes:
        #     print(f"Char: {node.char} -> val: {node.value}")

        while len(sorted_nodes) >= 2:

            left = sorted_nodes.pop(0)
            right = sorted_nodes.pop(0)

            parent_node = TreeNode(
                char="", value=(left.value + right.value), left=left, right=right
            )
            sorted_nodes.append(parent_node)

            sorted_nodes = self.sort(sorted_nodes)

        return sorted_nodes[0]

    def traverse_tree(self, root: TreeNode, bit_value: str = "") -> None:
        """Traverses the tree from a given root and create the encoding table"""

        if root.left == None and root.right == None:
            # it is a leaf node
            self.table[root.char] = bit_value

        if root.left is not None:
            self.traverse_tree(root.left, bit_value=bit_value + "0")

        if root.right is not None:
            self.traverse_tree(root.right, bit_value=bit_value + "1")

    def encode(self):
        """Encodes the input string and prints the huffman encoding table for all the characters"""
        self.traverse_tree(self.root)        

    def __str__(self) -> str:
        result = ["Huffman Encoding\n============="]
        for k, v in self.table.items():
            result.append(f"{k} = {v}")
        
        return "\n".join(result)

    def sort(self, array):
        """Sorts the array based the frequency value of the tree node"""
        return sorted(array, key=lambda x: x.value)

    def show_freq(self):
        """Prints the frequency of the characters"""
        print("Frequency table")
        print("===============")
        for k, v in self.freq2char.items():
            print(f"{k} = {v}")
        print()

obj = HuffmanEncoding("this is an example of a huffman tree")
obj.encode()

obj.show_freq()
print(obj)
# obj.show_freq()
