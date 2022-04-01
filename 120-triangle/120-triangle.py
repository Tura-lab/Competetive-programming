class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[-1 for n in range(len(triangle[-1]))] for i in range(len(triangle))]
        
        def solve(row, i):
            if dp[row][i] != -1:
                return dp[row][i]
            
            if row == len(triangle)-1:
                return triangle[row][i]
            
            left = solve(row+1, i)
            right = solve(row+1, i+1)
            
            dp[row][i] = min(left, right) + triangle[row][i]
            return dp[row][i]
            # return min(left, right) + triangle[row][i]
    
        return solve(0,0)