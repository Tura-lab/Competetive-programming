class Solution:
    '''
    [["1","1","1","1","0"],
     ["1","1","1","1","0"],
     ["1","1","1","1","1"],
     ["1","1","1","1","1"],
     ["0","0","1","1","1"]]
     
     [[1, 1, 1, 1, 0], 
      [1, 4, 4, 4, 0], 
      [1, 4, 16, 16, 1], 
      [1, 4, 16, 64, 4], 
      [0, 0, 1, 4, 16]]


      '''
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row, col = len(matrix), len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        
        ans = 0
        for i in range(row):
            for j in range(col):
                if i==0 or j==0:
                    dp[i][j] = int(matrix[i][j])
                    ans = max(ans, dp[i][j])
        
        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    if dp[i][j-1]>0 and dp[i-1][j-1]>0 and dp[i-1][j]>0:
                        dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])
                    else:
                        dp[i][j] = 1
                    
                    ans = max(ans, dp[i][j])
                        
        return ans*ans