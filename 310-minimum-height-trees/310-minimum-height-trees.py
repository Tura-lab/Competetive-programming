class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if not edges:
            return [0]
        if n<=2:
            return edges[0]
        graph = [[]for _ in range(n)]
        indeg = [0]*n
        
        for i, j in edges:
            indeg[i] += 1
            indeg[j] += 1
            graph[i].append(j)
            graph[j].append(i)
            
        q = collections.deque()
        for i in range(n):
            if indeg[i] == 1:
                q.append(i)
            
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                count += 1

                for v in graph[node]:
                    indeg[v] -= 1
                    if indeg[v] == 1:
                        q.append(v)
            
            if n-count <= 2:
                return q
            
                
            