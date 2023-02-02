class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        # counts = counter(nums)
        
        n = len(nums)
        
        decrement = 0
        count = 0
        
        zeros = nums.count(0)
        total = sum(nums)
        
        heap = []
        
        for num in set(nums): heappush(heap, num)
            
        while total and heap:
            while heap[0] == 0:
                heappop(heap)
            
            val = heappop(heap)
            total -= (val - decrement) * n
            
            decrement += val
            
            count += 1
            
        return count