class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for _ in range(n)]
        
        incomming = {i:0 for i in range(n)}
        outgoing = {i:set() for i in range(n)}
        
        for fro, to in edges:
            incomming[to] +=1
            outgoing[fro].add(to)
            
        q = collections.deque()
        
        for key in incomming.keys():
            if incomming[key] == 0:
                q.append(key)
                
        while q:
            node = q.popleft()
            
            for v in outgoing[node]:
                answer[v].update(answer[node])
                answer[v].add(node)
                incomming[v] -=1
                if incomming[v] ==0:
                    q.append(v)
        

        return [sorted(ans) for ans in answer]