# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, end: int) -> str:
        def dfs(node):
            if not node:
                return None
            if node.val in (start, end):
                return node
                
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left and right:
                return node
            
            return left or right
        
        self.s = []
        path = []
        par = dfs(root)
        def dfs(node):
            if not node:
                return 
            if node.val == end:
                self.s = path[:]
            
            path.append('L')
            dfs(node.left)
            path.pop()
            
            path.append('R')
            dfs(node.right)
            path.pop()
                
        dfs(par)
        path = []
        self.e = []
        def dfs(node):
            if not node:
                return 
            if node.val == start:
                self.e = path[:]
                return
            
            path.append('U')
            dfs(node.left)
            dfs(node.right)
            path.pop()
            
        dfs(par)
        return ''.join(self.e + self.s)
            
            
            
            