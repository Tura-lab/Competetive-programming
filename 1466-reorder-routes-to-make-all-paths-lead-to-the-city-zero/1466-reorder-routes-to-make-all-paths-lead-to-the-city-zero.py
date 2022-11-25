class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for a,b in connections:
            graph[a].append((b,-1))
            graph[b].append((a,1))
            
        count = 0
        def dfs(node, parent):
            nonlocal count
            for v, flag in graph[node]:
                if v == parent:continue
                    
                count += flag == -1
                
                dfs(v, node)
        
        dfs(0, -1)
        return count