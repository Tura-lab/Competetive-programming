class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        count = 0
        dp = [1] * n
        for i in range(1, n):
            if i-1 == 0 or nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] += dp[i-1]
            else:
                dp[i] += 1
                
            if dp[i] >= 3:
                count += dp[i] - 3 + 1
        
        return count