
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepth(self, root: TreeNode) -> int:
        
        return self.traversal(root)
        return self.bfs(root)
    
    def bfs(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        level = [root]
        depth = 0
        
        while level:
            
            depth += 1
            queue = []
            
            for node in level:
                
                if node.left != None:
                    queue.append(node.left)
                    
                if node.right != None:
                    queue.append(node.right)
                
            level = queue
            
        return depth
    
    def traversal(self, root: TreeNode) -> int:
        
        if root == None:
            return 0
        
        def traverse(node:TreeNode, prev_:int=1):
            
            if node == None:
                
                return prev_
            
            if node.right == None and node.left == None:
                print(f"Leaf node reached. Depth= {prev_}")
                return prev_
            
            return max(traverse(node.right, prev_+1),traverse(node.left, prev_+1))
        
        result = traverse(root)
        print('Final Result= ',result)
        
        return result