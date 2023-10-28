# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        def dfs(node, cur):
            if not node:
                return
            
            if len(ans) <= cur:
                ans.append(node.val)
            else:
                ans[cur] = max(ans[cur], node.val)
            
            dfs(node.left, cur + 1)
            dfs(node.right, cur + 1)
            
        dfs(root, 0)
        
        return ans