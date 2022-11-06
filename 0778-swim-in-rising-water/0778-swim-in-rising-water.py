class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def in_bound(i,j):
            return -1<i<rows and -1<j<cols
        
        def check(num):
            q = deque([(0,0)])
            visited = set([(0,0)])
            
            while q:
                i,j = q.popleft()
                
                if (i,j) == (rows-1, cols-1):
                    return True
                
                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nx, ny = x+i, y+j
                    if in_bound(nx,ny) and (nx,ny) not in visited and grid[nx][ny] <= num:
                        visited.add((nx,ny))
                        q.append((nx,ny))
                
            return False
            
        
        l = grid[0][0]
        r = max(max(grid[i]) for i in range(rows))
        
        ans = r
        
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                ans = mid
                r = mid-1
            else:
                l = mid + 1
        
        return ans