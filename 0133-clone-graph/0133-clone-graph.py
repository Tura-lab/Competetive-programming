"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        visited = dict()
        def dfs(node):
            if not node:
                return
            clone_node = Node(node.val)
            
            visited[node.val] = clone_node
            
            for v in node.neighbors:
                if v.val not in visited:
                    clone_node.neighbors.append(dfs(v))
                else:
                    clone_node.neighbors.append(visited[v.val])
                
            return clone_node
        
        return dfs(node)