class Solution:
    '''
    dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost))]
        dp[0] = cost[0]
        dp[1] = cost[1]
        
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
        # print(dp)
        return min(dp[-1], dp[-2])
        
#         dp = [-1]*len(cost)
#         def dfs(i):
#             if i>=len(cost):
#                 return 0
#             if dp[i] != -1:
#                 return dp[i]
            
            
#             dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
#             return dp[i]
        
        
#         return min(dfs(0), dfs(1))