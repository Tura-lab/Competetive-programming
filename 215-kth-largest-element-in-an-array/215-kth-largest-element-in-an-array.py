from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]*=-1
        heapify(nums)
        
        for i in range(k-1):
            heappop(nums)
            
        return -nums[0]
        