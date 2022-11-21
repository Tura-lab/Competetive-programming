class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        
        
        def in_bound(row,col):
            return -1<row<rows and -1<col<cols
                
        entrance = tuple(entrance)
        
        q = deque([(entrance[0], entrance[1])])
        visited = set([(entrance[0], entrance[1])])
        
        steps = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                
                if (x,y) != entrance and (x == rows-1 or x == 0 or y == 0 or y == cols-1):
                    return steps
                
                for a,b in directions:
                    nx, ny = a+x, b+y
                    if (nx, ny) not in visited and in_bound(nx, ny) and maze[nx][ny] == '.':
                        q.append((nx, ny))
                        visited.add((nx, ny))
                        
            steps += 1            
            
        return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            