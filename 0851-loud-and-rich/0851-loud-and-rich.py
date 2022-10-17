class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        parents = [set([_]) for _ in range(len(quiet))]
        
        graph = [[]for _ in range(len(quiet))]
        indeg = [0]*len(quiet)
        
        for a,b in richer:
            graph[a].append(b)
            indeg[b] += 1
        
        q = deque()
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
                
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for v in graph[node]:
                    for x in parents[node]:
                        parents[v].add(x)
                    indeg[v] -=1
                    if indeg[v] == 0:
                        q.append(v)
        
        ans =[]
        for i in range(len(quiet)):
            mn = quiet[i]
            man = i
            for v in parents[i]:
                if quiet[v] < mn:
                    mn = quiet[v]
                    man = v
                
            ans.append(man)
        return ans