class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        
        n = len(graph)
        colors = [0]*n
        
        def check(node):
            q = deque([node])
            color=1
            colors[node] = color
            
            while q:
                for _ in range(len(q)):
                    node = q.popleft()

                    for v in graph[node]:
                        if colors[v] == 0:
                            colors[v] = -color
                            q.append(v)
                        elif colors[v]==color:
                            return False
                color = -color

            return True
    
        for i in range(n):
            if colors[i]==0:
                if not check(i):
                    return False
        return True