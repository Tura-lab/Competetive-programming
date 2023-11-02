# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0, 0, 0
            
            l_count, l_sum, l_ans = dfs(node.left)
            r_count, r_sum, r_ans = dfs(node.right)
            
            tot_sum = l_sum + r_sum + node.val
            tot_count = l_count + r_count + 1
            
            ans = tot_sum // tot_count == node.val
            
            return tot_count, tot_sum, ans + l_ans + r_ans
            
        return dfs(root)[-1]