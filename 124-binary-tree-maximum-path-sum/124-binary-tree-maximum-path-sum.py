# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        def dfs(node):
            if not node:
                return -float("inf")
            
            left_tree = dfs(node.left)
            right_tree = dfs(node.right)
            
            self.ans = max(self.ans, node.val+left_tree+right_tree, right_tree, left_tree, node.val, node.val+left_tree, node.val+right_tree)
            
            return max(node.val, node.val+left_tree, node.val+right_tree)
            
        dfs(root)
        return self.ans