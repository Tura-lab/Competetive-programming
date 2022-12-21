class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n+1)]
        
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
            
        
        colors = [-1] * (n+1)
        def dfs(node, parent, color):
            if not node:
                return True
            
            if colors[node] == 1-color:
                return False
            
            colors[node] = color
            
            for v in graph[node]:                    
                if colors[v] == color or (colors[v] == -1 and not dfs(v, node, 1-color)):
                    return False
                
            return True
        
        for node in range(1, n+1):
            if colors[node] == -1:
                if not dfs(node, -1, 1):
                    return False
        
        return True
                
            