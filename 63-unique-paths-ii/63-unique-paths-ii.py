class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row = len(obstacleGrid)
        col = len(obstacleGrid[0])
        
        
        for i in range(row):
            for j in range(col):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue
                if i==0 and j==0:
                    obstacleGrid[i][j] = 1
                
                if -1<j-1<col:
                    obstacleGrid[i][j] += obstacleGrid[i][j-1]
                if -1<i-1<row:
                    obstacleGrid[i][j] += obstacleGrid[i-1][j]
        
        return obstacleGrid[i][j]
        
        
        
        
        
        
        
        
        
        
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