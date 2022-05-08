class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])        
        
        def dfs(row,col):
            if -1<row<rows and -1<col<cols and grid[row][col]==1:
                grid[row][col] = 0
                dfs(row-1,col)
                dfs(row+1,col)
                dfs(row,col-1)
                dfs(row,col+1)
                
        
        for i in range(rows):
            dfs(i,0)
            
        for i in range(rows):
            dfs(i,cols-1)
        
        for i in range(cols):
            dfs(0, i)
            
        for i in range(cols):
            dfs(rows-1, i)
            
        count=0
        # print(grid)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count+=1
        
        return count