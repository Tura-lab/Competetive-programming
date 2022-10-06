class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        '''
        [1,1,-1]
        [1,-1,1]
        [-1,1,1]
        
        [1,1]
        [1,0]
        '''
        n = len(grid)
        @cache
        def dfs(r1, c1, r2, c2):
            if not(-1<r1<n and -1<r2<n and -1<c1<n and -1<c2<n):
                return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == c1 == n-1 or r2 == c2 == n-1:
                return grid[r1][c1]
            
            old1 = grid[r1][c1]
            old2 = grid[r2][c2]
            grid[r1][c1] = grid[r2][c2] = 0
            ans = old1 if r1==r2 and c1==c2 else old1+old2
            
            found = float('-inf') 
            for a,b in [[1,0],[0,1]]:
                for c,d in [[1,0],[0,1]]:
                    found = max(found, dfs(r1+a, c1+b, r2+c, c2+d))
                    
            grid[r1][c1] = old1
            grid[r2][c2] = old2
            return ans + found
        
        
        ans = dfs(0,0,0,0)
        return 0 if ans == float('-inf') else ans