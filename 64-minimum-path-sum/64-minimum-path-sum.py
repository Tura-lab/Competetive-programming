class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[-1]*len(grid[0]) for _ in range(len(grid))]
        
        def dfs(row, col):
            if row>=len(grid) or col>=len(grid[0]):
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            
            if col+1>=len(grid[0]) and row+1>=len(grid):
                dp[row][col] = grid[row][col]
            elif col+1>=len(grid[0]):
                dp[row][col] = grid[row][col] + dfs(row+1, col)
            elif row+1>=len(grid):
                dp[row][col] = grid[row][col] + dfs(row, col+1)
            else:
                dp[row][col] =  grid[row][col] + min(dfs(row+1, col), dfs(row, col+1))
                
            return dp[row][col]
            
        return dfs(0,0)