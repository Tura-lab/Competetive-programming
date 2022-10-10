# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        found = {0:1}
        self.tot = 0
        def dfs(node):
            if not node:
                return 0
            
            self.tot += node.val
            if self.tot-targetSum in found:
                self.ans += found[self.tot-targetSum]
                
            if self.tot not in found:
                found[self.tot] = 1
            else:
                found[self.tot] += 1
            
            dfs(node.left)
            dfs(node.right)
            
            found[self.tot] -=1
            
            if found[self.tot] == 0:
                del found[self.tot]
                
            self.tot -= node.val
                
        dfs(root)
        return self.ans