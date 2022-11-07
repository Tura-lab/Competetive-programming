class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        '''
        [0,2,0,0,1]
        [0,2,0,2,2]
        [0,2,0,0,0]
        [0,0,2,2,0]
        [0,0,0,0,0]
        '''
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def in_bound(row,col):
            return -1<row<rows and -1<col<cols
        
        distances = {(i,j): float('inf') for i in range(rows) for j in range(cols)}
        
        fire_q = deque()
        fire_cells = set()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fire_cells.add((i,j))
                    fire_q.append((i,j))
            
        count = 0
        while fire_q:
            for _ in range(len(fire_q)):
                r,c = fire_q.popleft()
                distances[(r,c)] = count
                
                for x,y in directions:
                    nx,ny = x+r, y+c
                    if in_bound(nx,ny) and (nx,ny) not in fire_cells and grid[nx][ny] == 0:
                        fire_cells.add((nx,ny))
                        fire_q.append((nx,ny))
            
            count += 1

        def check(time):
            man_q = deque([(0,0)])
            man_cells = set([(0,0)])
            
            count = 0
            while man_q:
                for _ in range(len(man_q)):
                    r,c = man_q.popleft()
                    if distances[(r,c)] <= time+count and (r,c) != (rows-1, cols-1):
                        continue
                    
                    if (r,c) == (rows-1, cols-1) and distances[(r,c)] >= time+count:
                        return True
                    
                    for x,y in directions:
                        nx,ny = x+r, y+c
                        if in_bound(nx,ny) and (nx,ny) not in man_cells and grid[nx][ny] == 0 and distances[(nx,ny)] > time+count:
                            man_q.append((nx,ny))
                            man_cells.add((nx,ny))
            
                count += 1
                
            return False
        
        
        l, r = 0, 10**9
        
        ans = -1
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1

            
        return ans
