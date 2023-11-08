"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        
        def dfs(l, r):
            if not l:
                return
            
            dfs(l.left, l.right)
            dfs(r.left, r.right)
            
            l.next = r
            dfs(l.right, r.left)
            
        
        dfs(root.left, root.right)
        
        
        return root
        
        