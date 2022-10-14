class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        parents = [set() for _ in range(numCourses)]
        indeg = [0]*numCourses
        graph = [[]for _ in range(numCourses)]
        
        for a,b in prerequisites:
            graph[a].append(b)
            indeg[b] += 1
            
        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
                
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                for v in graph[node]:
                    parents[v].add(node)
                    for x in parents[node]:
                        parents[v].add(x)
                    
                    indeg[v] -=1
                    if indeg[v] == 0:
                        q.append(v)
        
        return  [u in parents[v] for u,v in queries]