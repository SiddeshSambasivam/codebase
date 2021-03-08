from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: TreeNode) -> List[List[int]]:
    
    dq = deque()
    
    if root: 
        dq.append(root)
        
    result = []
    while dq:
        
        level_nodes, level = [], len(dq)
        
        for _ in range(level):
            
            node = dq.popleft()
            
            if node != None:            
                level_nodes.append(node.val)
            
            if node.left != None:
                dq.append(node.left)
                
            if node.right != None:
                dq.append(node.right)
            
        result.append(level_nodes)
    
    return result

def create_tree(nodes: List[TreeNode]) -> TreeNode:

    for i, node in enumerate(nodes):

        # 2*i + 1 -> left child
        # 2*i + 2 -> right child

        l_idx, r_idx = 2*i+1, 2*i+2 

        if l_idx < len(nodes):
            node.left = nodes[l_idx]

        if r_idx < len(nodes):
            node.right = nodes[r_idx]

    return nodes[0]

def create_nodes(nodes:list) -> List[TreeNode]:

    return [TreeNode(val=v) if v!= "null" else None for v in nodes ]

def traverse(root:TreeNode):

    if root != None:

        print(f"Root: {root.val}")
        if root.left != None:
            print(f"Left child: {root.left.val}")
        if root.right != None:
            print(f"Right child: {root.right.val}")

        traverse(root.left)
        traverse(root.right)

def main(nodes:list):

    tree_nodes = create_nodes(nodes)    
    root = create_tree(tree_nodes)
    
    traverse(root)

    print(levelOrder(root))

main([3,9,20,"null","null",15,7])



