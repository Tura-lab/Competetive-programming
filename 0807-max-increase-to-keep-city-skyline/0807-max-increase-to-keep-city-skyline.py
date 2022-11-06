class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_rows = []
        max_cols = []
        
        for i in range(rows):
            max_rows.append(max(grid[i]))
        
        for j in range(cols):
            max_cols.append(max(grid[i][j] for i in range(rows)))
        
        ans = 0
        for i in range(rows):
            for j in range(cols):
                val = min(max_rows[i], max_cols[j])
                if val > grid[i][j]:
                    ans += val - grid[i][j]
        
        return ans
        