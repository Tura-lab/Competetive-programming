class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        dp = [[0 for _ in range(col)] for k in range(row)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                    
                if -1<j-1<col:
                    dp[i][j] += dp[i][j-1]
                if -1<i-1<row:
                    dp[i][j] += dp[i-1][j]
        
        return dp[-1][-1]
        
        
        
        
        
        
        
        
        
        
#         row = len(obstacleGrid)
#         col = len(obstacleGrid[0])
        
#         if obstacleGrid[-1][-1] == 1:
#             return 0
        
#         dp = [[-1 for _ in range(col)] for k in range(row)]
#         def dfs(i,j):
#             if i==row-1 and j==col-1:
#                 return 1
#             if not (-1<i<row and -1<j<col) or obstacleGrid[i][j] == 1:
#                 return 0
#             if dp[i][j]!=-1:
#                 return dp[i][j]
            
#             dp[i][j] = dfs(i+1,j) + dfs(i,j+1)
#             return dp[i][j]
        
#         return dfs(0,0)