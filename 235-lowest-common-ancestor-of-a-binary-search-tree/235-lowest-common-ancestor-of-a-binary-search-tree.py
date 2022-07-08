# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(root):
            if not root or root==p or root==q:
                return root

            left  = solve(root.left)
            right = solve(root.right)

            if right and left:
                return root
            if right:
                return right
            if left:
                return left
                
                
        return solve(root)