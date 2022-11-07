class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rows, cols = row, col
        
        for i in range(len(cells)):
            cells[i][0] -=1
            cells[i][1] -=1
        
        cells = {tuple(cells[i]): i+1 for i in range(len(cells))}
        
        def in_bound(row,col):
            return -1<row<rows and -1<col<cols
        
        # land is zero and water is one weird
        def check(day):
            q = deque()
            visited = set()
            for j in range(cols):
                if cells[(0,j)] > day:
                    visited.add((0,j))
                    q.append((0,j))
                    
            while q:
                r,c = q.popleft()
                
                if r == rows-1:
                    return True
                
                for x,y in [[1,0],[0,1],[0,-1],[-1,0]]:
                    nx, ny = x+r, y+c
                    if in_bound(nx,ny) and (nx,ny) not in visited and cells[nx,ny] > day:
                        visited.add((nx,ny))
                        q.append((nx,ny))
            
            return False
        
        ans = 0
        l, r = 0, rows*cols
        
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
            