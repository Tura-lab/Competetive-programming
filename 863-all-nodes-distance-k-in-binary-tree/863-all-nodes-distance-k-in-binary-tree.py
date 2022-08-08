# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        def dfs(root, parent):
            if not root:return
            
            if parent:
                graph[root].add(parent)
                graph[parent].add(root)
            
            dfs(root.left,  root)
            dfs(root.right, root)
    
        dfs(root, None)
        
        q = collections.deque()
        q.append(target)
        
        dist = 0
        while q and dist < k:            
            for _ in range(len(q)):
                node = q.popleft()
                for v in graph[node]:
                    graph[v].remove(node)
                    q.append(v)
            dist += 1
            
        return [v.val for v in q]
    
            