class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        ans = [0]*(n+1)
        graph = [[]for _ in range(n+1)]
        indeg = [0]*(n+1)
        
        for a,b in relations:
            graph[a].append(b)
            indeg[b] += 1
        
        q = deque()
        for i in range(1, n+1):
            if indeg[i] == 0:
                ans[i] = time[i-1]
                q.append(i)
        
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                t = ans[node]
                for v in graph[node]:
                    ans[v] = max(ans[v], t + time[v-1])
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)
                
                
                
        return max(ans)
                