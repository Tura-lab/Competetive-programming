class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = []
        ans = max(nums)
        
        for i, num in enumerate(nums):
            while heap and i - heap[0][1] > k:
                heappop(heap)
        
            val = 0 if not heap else -heap[0][0]
            
            new_num = max(num, num + val)
            ans = max(ans, new_num)
            
            heappush(heap, (-new_num, i))
        
        
        return ans