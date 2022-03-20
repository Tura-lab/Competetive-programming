"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def depth(root):
            if not root or not root.children:
                return 1
            ans = 0
            for child in root.children:
                ans = max(ans, 1 + depth(child))

            return ans
        return depth(root)