class UnionFind:
    def __init__(self, n):
        self.reps = []


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(i, j):
            if not(-1<i<len(grid) and -1<j<len(grid[0])) or grid[i][j]==0 or (i,j) in visited:
                return 0
            
            visited.add((i,j))
            ans = 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j-1) + dfs(i, j+1)
            
            return ans
        area = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(dfs(i,j), area)
        
        return area
        
        