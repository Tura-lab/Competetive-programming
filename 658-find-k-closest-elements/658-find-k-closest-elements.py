class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        
        for num in arr:
            heapq.heappush(heap, (abs(x-num), num))
            
        return sorted([heapq.heappop(heap)[1] for _ in range(k)])