"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        ans = []
        if not root: return ans
        
        q = collections.deque()
        q.append(root)
        
        level = [root.val]
        while q:
            ans.append(level)
            for _ in range(len(q)):
                node = q.popleft()
                for v in node.children:
                    q.append(v)
            
            level = [n.val for n in q]

        return ans