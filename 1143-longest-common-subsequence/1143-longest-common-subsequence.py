from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1]*(m+1) for _ in range(n+1)]
        for j in range(m+1):
            dp[0][j] = 0 
            
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                print(j,i)
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[n][m]
        
        
        
        
        
        # print(n,m)
        
#         @lru_cache(1000000)
#         def dfs(i,j):
#             if i>=m or j>=n:
#                 return 0
            
#             if text1[i] == text2[j]:
#                 return 1+dfs(i+1, j+1)
            
#             return max(dfs(i+1,j), dfs(i,j+1))
        
#         return dfs(0,0)