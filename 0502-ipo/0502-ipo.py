class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxHeap = []
        
        projects = sorted(list(zip(capital, profits)))
        
        # If we can afford anything
        if projects[-1][0] <= w:
            return sum(sorted(profits, reverse=True)[:k]) + w
        
        i = 0
        print(k)
        while k:
            while i < len(projects) and projects[i][0] <= w:
                heappush(maxHeap, -projects[i][1])
                i += 1
                
            if maxHeap:
                print(w)
                w += -heappop(maxHeap)
                print(w)
                k -= 1
            else:
                return w
            
        return w