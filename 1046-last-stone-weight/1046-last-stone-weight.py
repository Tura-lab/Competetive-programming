from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]*=-1
            
        heapify(stones)
        
        while len(stones) > 1:
            x = -heappop(stones)
            y = -heappop(stones)
            
            if x!=y:
                heappush(stones, -abs(x-y))
        return -stones[0] if stones else 0
            