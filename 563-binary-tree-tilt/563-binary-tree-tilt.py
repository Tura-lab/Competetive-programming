# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = [0]
        def tilt(root):
            if not root:
                return 0
            if not root.left and not root.right:
                num = root.val
                root.val = 0
                return num
            
            if not root.left:
                leftSum = 0
            else:
                leftSum  = root.left.val + tilt(root.left)
            
            if not root.right:
                rightSum = 0
            else:
                rightSum = root.right.val + tilt(root.right)
            
            num = root.val
            root.val = abs(rightSum-leftSum)
            ans[0] += root.val
            return rightSum + leftSum + num
        tilt(root)
        return ans[0]//2