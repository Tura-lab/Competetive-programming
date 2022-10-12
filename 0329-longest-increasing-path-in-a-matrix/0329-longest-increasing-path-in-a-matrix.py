class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        found = [[-1]*c for _ in range(r)]
        
        def dfs(i,j):
            if found[i][j] == -1:
                count = 1
                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    a,b = x+i,y+j
                    if -1<a<r and -1<b<c and grid[a][b] > grid[i][j]:
                        count = max(count, 1 + dfs(a,b))
                
                found[i][j] = count
            
            return found[i][j]
        
        for i in range(r):
            for j in range(c):
                dfs(i,j)
                
        return max(max(a) for a in found)