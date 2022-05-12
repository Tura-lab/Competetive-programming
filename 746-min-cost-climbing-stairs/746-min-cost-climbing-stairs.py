class Solution:
    '''
    dp[i] = cost[i] + min(dp[i-1], dp[i-2])
    '''
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1 for _ in range(len(cost))]
        first = cost[0]
        second = cost[1]
        ans = min(first, second)
        
        for i in range(2, len(cost)):
            ans = cost[i] + min(first, second)
            first = second
            second = ans
            
        return min(first, second)
        
#         dp = [-1]*len(cost)
#         def dfs(i):
#             if i>=len(cost):
#                 return 0
#             if dp[i] != -1:
#                 return dp[i]
            
            
#             dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
#             return dp[i]
        
        
#         return min(dfs(0), dfs(1))