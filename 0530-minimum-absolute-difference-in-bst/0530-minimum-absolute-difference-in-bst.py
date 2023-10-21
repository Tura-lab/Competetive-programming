# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        
        def push_left(node, stack):
            while node:
                stack.append(node)
                node = node.left
        
        push_left(root, stack)
        
        ans = float('inf')
        while stack:
            node = stack.pop()
            push_left(node.right, stack)
            if stack:
                ans = min(ans, abs(node.val - stack[-1].val))
                
        return ans