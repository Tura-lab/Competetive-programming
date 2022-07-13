"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        ans = []
        def dfs(node):
            for v in node.children:
                dfs(v)
            
            ans.append(node.val)
        
        
        if root: dfs(root)
        return ans
        