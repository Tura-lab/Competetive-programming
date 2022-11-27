class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        
        count = 0
        for j in range(n):
            for i in range(j):
                    
                dp[j][nums[j] - nums[i]] += + 1
                
                if nums[j] - nums[i] in dp[i]:
                    dp[j][nums[j] - nums[i]] += dp[i][nums[j] - nums[i]]
                    count += dp[i][nums[j] - nums[i]]
                
        return count