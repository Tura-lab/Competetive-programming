# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        found = []
        if not root:return []
        
        def dfs(node, tot):
            if not node:return
            if not (node.right or node.left):
                if tot+node.val == targetSum:
                    self.ans.append(found + [node.val])
                return
            
            found.append(node.val)
            dfs(node.right, tot+node.val)
            dfs(node.left, tot+node.val)
            found.pop()
        
        dfs(root, 0)
        return self.ans
                