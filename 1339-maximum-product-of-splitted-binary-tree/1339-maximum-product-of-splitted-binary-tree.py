# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        mod = 10 **9 +7
        
        def dfs(node):
            if not node:
                return 0
            
            return node.val + dfs(node.left) + dfs(node.right)

        total = dfs(root)
        
        self.ans = 0
        def dfs(node):
            if not node:
                return 0
            
            left  = dfs(node.left)
            right = dfs(node.right)
            
            cur = left + right + node.val
            
            self.ans = max(self.ans, (total - cur) * cur)
            
            return cur
            
        dfs(root)
        
        return self.ans % mod