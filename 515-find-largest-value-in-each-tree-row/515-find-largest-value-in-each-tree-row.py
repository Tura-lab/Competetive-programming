# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root):
        ans = []
        if not root:
            return []
        def counter(root, row):
            if not root:
                return 
            if row>len(ans):
                ans.append(root.val)
            else:
                ans[row-1] = max(ans[row-1], root.val)
            counter(root.left, row+1)
            counter(root.right, row+1)
            
        counter(root, 1)
        return ans

                
        