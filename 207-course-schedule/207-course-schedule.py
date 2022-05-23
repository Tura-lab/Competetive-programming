class Solution:
    def canFinish(self, n: int, pr: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        indeg = [0 for _ in range(n)]
        
        for i,j in pr:
            indeg[i] +=1
            graph[j].append(i)
            
        q = collections.deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)
            
        count = 0
        while q:
            node = q.popleft()
            count +=1
            for neigh in graph[node]:
                indeg[neigh] -=1
                if indeg[neigh] ==0:
                    q.append(neigh)
                    
                    
        return count == n
            
            