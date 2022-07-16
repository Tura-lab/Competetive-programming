class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        mod = 10**9 + 7
        @cache
        def dfs(row, col, movesLeft):
            if not (-1<row<m and -1<col<n):
                return 1
            if movesLeft == 0:
                return 0
            
            return (dfs(row+1, col, movesLeft-1) + dfs(row-1, col, movesLeft-1) + dfs(row, col+1, movesLeft-1) + dfs(row, col-1, movesLeft-1))%mod
        
        return dfs(startRow, startColumn, maxMove)