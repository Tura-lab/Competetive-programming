from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # dp = [[None for _ in range(len(nums))] for _ in range(len(nums))]
        # print(len(multipliers), len(nums))
        n, m = len(nums), len(multipliers)
        dp = [[0]*(m+1) for _ in range(m+1)]
        
        for tot in range(m-1, -1, -1):
            for i in range(tot, -1, -1):
                j = n - 1 - (tot - i)
                num = multipliers[tot]
                
                dp[tot][i] = max(nums[i]*num + dp[tot+1][i+1], nums[j]*num + dp[tot+1][i])
                
        return dp[0][0]
        
        
        
        
#         @lru_cache(2000)
#         def dfs(i,k):
#             j = len(nums)-1-(k-i)
#             if i>j or k>=len(multipliers):
#                 return 0

#             return max(nums[i]*multipliers[k] + dfs(i+1,k+1), nums[j]*multipliers[k] + dfs(i,k+1))
            
        
#         return dfs(0, 0)