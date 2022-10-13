# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, p):
            if not node:
                return (-float('inf'), float('inf'), 0)
            
            left  = dfs(node.left, node)
            right = dfs(node.right, node)
            
            if not left or not right:
                return False

            left_max, left_min, left_tot = left
            right_max, right_min, right_tot = right
            
            if left_max < node.val < right_min:
                self.ans = max(self.ans, node.val + right_tot + left_tot)
                new_min = min(node.val, left_min, right_min)
                new_max = max(node.val, left_max, right_max)
                # print((left_min,left_max), (right_min, right_max), new_min, new_max, node.val)
                return (new_max, new_min, node.val + left_tot + right_tot)
            else:
                return False
            
        dfs(root,None)
        return self.ans