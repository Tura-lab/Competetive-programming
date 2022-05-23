class Solution:
    def minNumberOfSemesters(self, n: int, r: List[List[int]], k: int) -> int:
        final = (2**n) -1
        graph = {i:[] for i in range(1,n+1)}
        indeg = {i:0 for i in range(1,n+1)}
        for i,j in r:
            graph[i].append(j)
            indeg[j] +=1
                
        @cache
        def solve(taken):
            toBeTaken = [i for i in range(1,n+1) if indeg[i]==0 and (taken & 1<<i)==0] 
            # print(toBeTaken)
            if not toBeTaken:
                return 0
            
            ans = float('inf')
            for pos in itertools.combinations(toBeTaken,min(k, len(toBeTaken))):
                old_t = taken
                for i in pos:
                    taken |= 1<<i
                for i in pos:
                    for neigh in graph[i]:
                        indeg[neigh]-=1
                
                ans = min(ans, 1+solve(taken))
                
                for i in pos:
                    for neigh in graph[i]:
                        indeg[neigh]+=1
                    
                taken = old_t
            
            return ans
        
        return solve(0)