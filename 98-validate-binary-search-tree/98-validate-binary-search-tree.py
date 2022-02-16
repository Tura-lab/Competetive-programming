# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root, lower = -math.inf, higher = math.inf):
        if not root:
            return True
        
        if root.val >= higher or root.val <= lower:
            return False

        return self.isValidBST(root.left, lower, root.val) and self.isValidBST(root.right, root.val, higher)