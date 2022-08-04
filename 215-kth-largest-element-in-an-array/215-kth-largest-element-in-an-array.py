class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        counts = {}
        for num in nums:
            counts[num] = 1 if num not in counts else counts[num]+1
        
        count = 0
        i=0
        for num in range(10000, -10001, -1):
            if num in counts:
                count += counts[num]
            if count>=k:
                return num