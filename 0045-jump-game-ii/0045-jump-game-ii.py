class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        
        dp[0] = 0
        
        for i in range(n):
            for j in range(1, min(n - i, nums[i] + 1)):
                dp[i + j] = min(dp[i + j], 1 + dp[i])
            
        # print(dp)
        return dp[-1]