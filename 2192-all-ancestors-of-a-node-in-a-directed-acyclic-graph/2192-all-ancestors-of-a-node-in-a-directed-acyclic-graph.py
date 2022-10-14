class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        parents = [set() for _ in range(n)]
        graph = [[] for _ in range(n)]
        indeg = [0]*n
        
        for a,b in edges:
            graph[a].append(b)
            indeg[b] += 1
        
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for v in graph[node]:
                    parents[v].add(node)
                    for x in parents[node]:
                        parents[v].add(x)
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
                    
            
            
        return [sorted(list(a)) for a in parents]