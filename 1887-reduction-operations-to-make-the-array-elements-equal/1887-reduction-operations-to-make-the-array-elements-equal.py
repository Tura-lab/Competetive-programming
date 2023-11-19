class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        ans = 0
        nums.sort(reverse=True)
        
        past, count = None, 0
        for num in nums:
            if num != past:
                ans += count
                past = num
            count += 1
            
        return ans