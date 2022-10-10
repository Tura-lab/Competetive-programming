class Solution:
    def numberOfPaths(self, grid: List[List[int]], num: int) -> int:
        '''
        [1,1,1]
        [1,1,1]
        [1,1,1]
        '''
        r,c = len(grid),len(grid[0])
        mod = 10**9 +7
        
        dp = [[[0]*num for _ in range(c+1)] for __ in range(r+1)]
        dp[1][1][grid[0][0]%num] = 1
        
        for i in range(1, r+1):
            for j in range(1, c+1):
                cur = grid[i-1][j-1]%num
                for k in range(num):
                    dp[i][j][(cur+k)%num] += (dp[i-1][j][k] + dp[i][j-1][k])%mod

        return dp[r][c][0]%mod