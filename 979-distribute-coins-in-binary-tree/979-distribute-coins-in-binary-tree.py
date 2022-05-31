# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def solve(root):
            if not root:
                return 0
            
            left = solve(root.left)
            right = solve(root.right)
            
            total_coins = left + right + root.val
            
            self.moves += abs(total_coins-1)
            
            return total_coins -1
        
        solve(root)
        return self.moves