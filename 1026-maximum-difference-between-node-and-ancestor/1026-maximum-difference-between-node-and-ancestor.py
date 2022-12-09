# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, mx, mn):
            if not node:
                return 
            
            mx = max(mx, node.val)
            mn = min(mn, node.val)
            
            self.ans = max(self.ans, abs(mx - mn))
            
            dfs(node.left, mx, mn)
            dfs(node.right, mx, mn)
            
        dfs(root, -float('inf'), float('inf'))
        
        return self.ans