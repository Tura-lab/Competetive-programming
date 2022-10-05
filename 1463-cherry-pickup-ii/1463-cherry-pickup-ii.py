class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r,c = len(grid), len(grid[0])
        dp = [[[0]*(c+2) for __ in range(c+2)] for _ in range(r+2)]
        for i in range(r, 0, -1):
            for j in range(1, c+1):
                for k in range(1, c+1):
                    for a in [1,0,-1]:
                        for b in [1,0,-1]:
                            dp[i][j][k] = max(dp[i][j][k], dp[i+1][j+a][k+b])
                    if j==k:
                        dp[i][j][k] += grid[i-1][j-1]
                    else:
                        dp[i][j][k] += grid[i-1][j-1] + grid[i-1][k-1]
        return dp[1][1][c]