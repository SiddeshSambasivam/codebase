"""
Implementation of Trie
Operations: Insertion, Deletion and Lookup

Data structure: Node, Trie

structure Node
    Children Node[Alphabet-Size]
    Is-Terminal Boolean
    Value Data-Type
end structure

"""
from typing import TypedDict, Type, List

class NodeChildren(TypedDict):
    char: str
    node: Type["Node"]

class Node(object):

    def __init__(self, char:str) -> None:
        """Initializes the node with the character"""
        self.char = char
        self.children: NodeChildren = NodeChildren()
        self.isEnd: bool = True
        self.word: str = ""
    
    def isChild(self, char: str) ->  bool:
        """Checks if given character is a child"""
        return char in self.children

    def addChild(self, char: str) -> None:
        """Add given char as a child"""
        charNode = Node(char)
        self.children[char] = charNode
        self.isEnd = False
        # print(f'Root: {self.char} \t Add new child: {self.children}')

    def __str__(self) -> str:
        return f"<Node char={self.char}>"

    def __repr__(self) -> str:
        return f"<Node char={self.char}>"


class Trie:

    def __init__(self) -> None:
        self.root = Node("")

    def add(self, word: str) -> None:
        """Add the word to the trie"""        
        curNode = self.root

        for i in range(len(word)):
            char = word[i]
            if curNode.isChild(char) is False:
                curNode.addChild(char)
            
            curNode = curNode.children[char]

    def getLongestWord(self) -> str:
        """Returns the longest word in the trie"""
        # traverse through the tree and check word with max len
        result = ""

        stack = [self.root]
        explored = [self.root]

        while stack:

            node = stack.pop(0)
            if node.isEnd:
                if len(node.word) > len(result):
                    result = node.word
            
            for _, child in node.children.items():
                if child not in explored:
                    child.word = node.word + child.char
                    stack.append(child)
                    explored.append(child)

        return result

# add(ap)
# node: children
# root: [a]
# a: [p]

# add(apple)
# node: children
# root: [a]
# a: [p]
# p: [p]
# p: [l]
# l: [e]

# add(apply)
# node: children
# root: [a]
# a: [p]
# p: [p]
# p: [l]
# l: [e, y]

if __name__ == "__main__":

    t = Trie()
    # words: List[str] = ["ap", "apply", "apple"]
    # words = ["w","wo","wor","worl","world"]
    words = ["a","banana","app","appl","ap","apply","apple"]
    words.sort()
    
    for word in words:
        t.add(word)

    print(t.getLongestWord(), '\n')
    


        

            

