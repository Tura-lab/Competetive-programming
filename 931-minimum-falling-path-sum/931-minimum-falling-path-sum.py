class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix), len(matrix[0])
        dp = [[float('inf')]*(c+2) for _ in range(r+2)]
        dp[-1] = [0]*(c+2)
        
        for i in range(r, 0, -1):
            for j in range(1, c+1):
                for a in [-1,0,1]:
                    dp[i][j] = min(dp[i][j], dp[i+1][j+a])
                    
                dp[i][j] += matrix[i-1][j-1]
        
        # for d in dp:print(d)
        
        return min(dp[1])