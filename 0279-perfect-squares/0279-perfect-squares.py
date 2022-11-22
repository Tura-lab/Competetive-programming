class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        
        powers = {i : i**2 for i in range(ceil(sqrt(n+1)))}
        
        for i in range(1, n+1):
            for j in range(ceil(sqrt(n+1))):
                dp[i] = min(dp[i], 1 + dp[i - powers[j]])
                
        return dp[-1]