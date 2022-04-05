class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n)]
        
        def solve(i):
            if i==n:
                return 1
            if i>n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            one_step  = solve(i+1)
            two_steps = solve(i+2)                
            
            dp[i] = one_step + two_steps
            return dp[i]
        
        return solve(0)