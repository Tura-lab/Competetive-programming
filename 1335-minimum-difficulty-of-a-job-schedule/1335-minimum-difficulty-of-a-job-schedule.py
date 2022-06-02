class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        if d>n:
            return -1
        
        dp = [[-1]*(n) for _ in range(n)]
        
        def solve(i, day, dif,j):
            if i==n:
                return dif
            
            if dp[j][day] == -1:
                cut = float('inf')
                if day<d:
                    cut = dif + solve(i+1, day+1, jobDifficulty[i],i)

                dont = float('inf')
                if n-i-1 >= d-day:
                    dont = solve(i+1, day, max(dif, jobDifficulty[i]),j)
                
                dp[j][day] = min(cut, dont)
                
            return dp[j][day]

        return solve(1, 1, jobDifficulty[0],0)