class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total = sum(piles)
        heap = []
        
        for pile in piles:
            heappush(heap, -pile)
            
        
        while k and heap:
            pile = -heappop(heap)
            cur = pile // 2
            
            total -= cur
            heappush(heap, -1*(pile-cur))
            k-=1
            
        return total