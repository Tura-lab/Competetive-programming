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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        levels = []
        def helper(root,level):
            if not root:
                return
            if len(levels) <= level:
                levels.append(deque())
            
            if levels[level]:
                levels[level][0].next = root
                levels[level].popleft()
            levels[level].append(root)
            helper(root.left, level+1)
            helper(root.right, level+1)
        
        helper(root, 0)
        return root
            