# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node.left and not node.right:
                cur.append(str(node.val))
                self.ans += int("".join(cur))
                cur.pop()
                return 
            
            cur.append(str(node.val))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
                
            cur.pop()

        cur = []
        dfs(root)
        
        return self.ans