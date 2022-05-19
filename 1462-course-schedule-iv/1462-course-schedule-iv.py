class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        reached_by = [set() for _ in range(n)]
        
        incomming = [0]*n
        outgoing  = [set() for _ in range(n)] 
        
        for fro, to in prerequisites:
            incomming[to] += 1
            outgoing[fro].add(to)

        q = collections.deque()
        
        for key in range(n):
            if incomming[key] == 0:
                q.append(key)
                
        while q:
            node = q.popleft()
            
            for v in outgoing[node]:
                reached_by[v].add(node)
                
                incomming[v]-=1
                if incomming[v] == 0:
                    q.append(v)
                
                for past in reached_by[node]:
                    reached_by[v].add(past)
        
        # print(reached_by)
        return [u in reached_by[v] for u,v in queries]
            