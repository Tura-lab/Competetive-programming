class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n)
        
        dp[0] = 1
        dp[1] = min(dp[0], dp[1])
        
        for i in range(n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
        return min(dp[-1], dp[-2])