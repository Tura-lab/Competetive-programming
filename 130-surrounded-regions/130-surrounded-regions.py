class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        seen = set()
        seen2 = set()
        rows, cols = len(grid), len(grid[0])
        
        def all_paths_lead_to_x(row,col):
            if not(-1<row<rows and -1<col<cols):
                return False
            if grid[row][col] == 'X' or (row,col) in seen:
                return True
            seen.add((row,col))
            left = all_paths_lead_to_x(row,col-1)
            up = all_paths_lead_to_x(row-1,col)
            right = all_paths_lead_to_x(row,col+1)
            bottom = all_paths_lead_to_x(row+1,col)
            return left and up and right and bottom
        
        def dfs(row,col):
            if (row,col) in seen2 or not(-1<row<rows and -1<col<cols) or grid[row][col] == 'X':
                return
            seen2.add((row,col))
            grid[row][col] = 'X'
            dfs(row,col-1)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row+1,col)
        
        for row in range(rows):
            for col in range(cols):
                if (row,col) not in seen and grid[row][col] == 'O' and all_paths_lead_to_x(row,col):
                    seen.add((row,col))
                    dfs(row,col)
                    
                    