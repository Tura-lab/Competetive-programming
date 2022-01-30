# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, left, right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        if left.val == right.val:
            l = self.check(left.left, right.right)
            r = self.check(left.right, right.left)
            return l and r
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)