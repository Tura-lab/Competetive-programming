# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(root, cur):
            
            if not root.right and not root.left:
                return cur *2 +root.val
            
            if not root.left:
                return dfs(root.right, cur*2 + root.val)
            if not root.right:
                return dfs(root.left, cur*2 + root.val)
            
            return dfs(root.right, cur*2 + root.val) + dfs(root.left, cur*2 + root.val)
        
        return dfs(root, 0)