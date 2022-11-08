class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        rows, cols = len(grid), len(grid[0])
        
        if (rows + cols - 1) & 1:
            return False
        
        def in_bound(row, col):
            return -1<row<rows and -1<col<cols
        
        @cache
        def dfs(row, col, count):
            if count < 0 or not in_bound(row,col):
                return False
            
            if grid[row][col] == ')':
                count -= 1
            else:
                count += 1
                
            if (row,col) == (rows-1, cols-1):
                return count == 0
            
            return dfs(row+1, col, count) or dfs(row, col+1, count)
        
        return dfs(0,0, 0)