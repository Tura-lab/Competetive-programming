"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        ans = []
        def helper(root,level):
            if not root:
                return 
            if len(ans)<=level:
                ans.append(deque())
            if ans[level]:
                ans[level][0].next = root
                ans[level].popleft()
            if root:
                ans[level].append(root)
            helper(root.left, level+1)
            helper(root.right, level+1)
        
        helper(root, 0)
        return root