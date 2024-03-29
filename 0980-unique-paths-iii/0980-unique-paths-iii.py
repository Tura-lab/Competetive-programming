class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.ans = 0
        r,c = len(grid),len(grid[0])
        
        total = (1 << ((r*c))) -1
        start = None
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == -1:
                    total ^= 1 << (i*c + j)
                if grid[i][j] == 1:
                    start = (i,j)
        
        def dfs(i,j,mask):
            # print(path)
            if mask == total:
                self.ans += grid[i][j] == 2
                return
            if grid[i][j] == 2:
                return
            
            for x,y in [[1,0],[-1,0],[0,1],[0,-1]]:
                nx,ny = i+x, j+y
                if -1<nx<r and -1<ny<c and grid[nx][ny] != -1 and (1 << (nx*c + ny)) & mask == 0:
                    # path.append((nx,ny))
                    dfs(nx, ny, mask | (1 << (nx*c + ny)))
                    # path.pop()
            
        # path = [(start[0], start[1])]
        dfs(start[0], start[1], 1 << (start[0]*c + start[1]))
        return self.ans
    