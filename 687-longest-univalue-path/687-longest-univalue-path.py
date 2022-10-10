# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, p):
            if not node:
                return 0
            
            left = dfs(node.left, node)
            right = dfs(node.right, node)
            
            self.ans = max(self.ans, 1+left+right)
            # print(node.val, (left,right))
            
            if not p or node.val == p.val:
                return 1 + max(left, right)
            
            return 0
            
        dfs(root, None)
        
        return self.ans-1 if self.ans else 0
    