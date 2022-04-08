# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        tot = [0]
        def solve(root, p=None, gp=None):
            if not root:
                return 
            if gp and gp.val %2 == 0:
                tot[0]+=root.val
            solve(root.left, root, p)
            solve(root.right, root, p)
            
        solve(root)
        return tot[0]
                
            