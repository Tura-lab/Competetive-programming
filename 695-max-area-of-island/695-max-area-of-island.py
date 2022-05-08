class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col):
            if not( -1<row<rows and -1<col<cols) or grid[row][col]!=1 or (row,col) in seen:
                return 0
            
            seen.add((row,col))
            return 1 + dfs(row, col-1) + dfs(row-1, col) + dfs(row, col+1) + dfs(row+1, col)
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen:
                    ans = max(ans, dfs(row,col))
                    
        return ans
        
        