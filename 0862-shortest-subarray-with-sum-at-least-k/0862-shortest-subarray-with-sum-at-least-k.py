class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        heap = []
        heappush(heap, (0, 1))
        ans = float('inf')
        
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum += num
            while heap and heap[0][0] <= cur_sum - k:
                sm, idx = heappop(heap)
                ans = min(ans, i + idx) # idx is negative in the heap
                
            heappush(heap, (cur_sum, -i))
            
        return ans if ans < float('inf') else -1