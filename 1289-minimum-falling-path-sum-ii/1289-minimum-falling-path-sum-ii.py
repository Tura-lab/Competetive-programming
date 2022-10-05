class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        '''
        [1,7,8,2,3],
        [4,1,2,5,6],
        [7,8,2,5,9],
        [1,4,3,2,3],
        [7,2,3,1,6]
        '''
#         r,c = len(grid),len(grid[0])
#         dp = [[[float('inf')]*(4) for __ in range(c+2)] for _ in range(r+2)]
        
#         for j in range(c+2):
#             for i in range(4):
                
        r,c = len(matrix), len(matrix[0])
        dp = [[float('inf')]*(c+2) for _ in range(r+2)]
        dp[-1] = [0]*(c+2)
        
        for i in range(r, 0, -1):
            for j in range(1, c+1):
                mn = min(min(dp[i+1][:j]), min(dp[i+1][j+1:]))
                dp[i][j] = mn + matrix[i-1][j-1]
        
        return min(dp[1])