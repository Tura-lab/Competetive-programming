class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        
        dp_even, dp_odd = 0, 0
        
        for i, num in enumerate(nums):
            dp_even = max(dp_even, dp_odd + num)
            dp_odd = max(dp_odd, dp_even - num)
        
        return max(dp_odd, dp_even)