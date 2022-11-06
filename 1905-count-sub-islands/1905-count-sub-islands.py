class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        
        def dfs(i, j):
            if grid1[i][j] != 1:
                self.ans = False
            
            for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx, ny = i+x, y+j
                if -1<nx<r and -1<ny<c and (nx,ny) not in visited and grid2[nx][ny] == 1:
                    visited.add((nx,ny))
                    dfs(nx, ny)
        
        
        r, c = len(grid1), len(grid1[0])
        
        ans = 0
        for i in range(r):
            for j in range(c):
                if (i,j) in visited:continue
                if grid2[i][j] == 1:
                    visited.add((i,j))
                    self.ans = True
                    dfs(i,j)
                    ans += self.ans
                
        return ans