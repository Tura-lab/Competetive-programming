class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        rows, cols = len(grid), len(grid[0])
        islands=0
        
        def dfs(row, col):
            if not (-1<row<rows and -1<col<cols) or grid[row][col]!='1':
                return
            
            if (row,col) not in seen and grid[row][col]=='1':
                seen.add((row, col))
                dfs(row, col-1)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row+1, col)
        
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in seen and grid[row][col]=='1':
                    dfs(row,col)
                    islands+=1
                    
        return islands
                    
        