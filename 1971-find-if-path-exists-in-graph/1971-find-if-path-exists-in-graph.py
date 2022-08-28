class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        visited = set()
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        ans = [False]
        
        def dfs(node):
            if node==end:
                ans[0] = True
                return 
            
            for v in graph[node]:
                if v not in visited:
                    visited.add(v)
                    dfs(v)
        
        dfs(start)
        return ans[0]