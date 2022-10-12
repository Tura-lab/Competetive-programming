# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, end: int) -> str:
        to_start = []
        to_end = []
        path = []
        def dfs(node):
            nonlocal to_start, to_end
            if not node:
                return
            
            if node.val == start:
                to_start = path[:]
            if node.val == end:
                to_end = path[:]
                
            path.append('L')
            dfs(node.left)
            path.pop()
            
            path.append('R')
            dfs(node.right)
            path.pop()
            
        dfs(root)
        i = 0
        while i<len(to_start) and i<len(to_end) and to_start[i] == to_end[i]:
            i+=1
            
        to_start=  to_start[i:]
        to_end = to_end[i:]
        to_start = ['U']*len(to_start)
        
        
        return ''.join(to_start + to_end)