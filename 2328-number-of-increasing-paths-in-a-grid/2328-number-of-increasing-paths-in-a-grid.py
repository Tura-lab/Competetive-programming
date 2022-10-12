class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        '''
        3,2,1
        3,2,1
        '''
        mod = 10**9 +7
        r,c = len(grid),len(grid[0])
        found = {}
        
        def dfs(i,j):
            if (i,j) not in found:
                count = 0
                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    a,b = x+i,y+j
                    if -1<a<r and -1<b<c and grid[a][b] > grid[i][j]:
                        count += 1 + dfs(a,b)
                
                found[(i,j)] = count
            
            return found[(i,j)]
        
        tot = 0
        for i in range(r):
            for j in range(c):
                tot += dfs(i,j)
                tot %= mod
                
        return (tot + r*c)%mod
            