class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.count = 0
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        self.minutes = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    self.count+=1
                elif grid[row][col] == 2:
                    q.append((row,col))
        
        while q and self.count:
            self.minutes+=1
            for _ in range(len(q)):
                row,col = q.popleft()
                if -1<row-1<rows and -1<col<cols and grid[row-1][col]==1:
                    self.count-=1
                    grid[row-1][col] = 2
                    q.append((row-1,col))
                if -1<row+1<rows and -1<col<cols and grid[row+1][col]==1:
                    self.count-=1
                    grid[row+1][col]=2
                    q.append((row+1,col))
                if -1<row<rows and -1<col-1<cols and grid[row][col-1]==1:
                    self.count-=1
                    grid[row][col-1]=2
                    q.append((row,col-1))
                if -1<row<rows and -1<col+1<cols and grid[row][col+1]==1:
                    self.count-=1
                    grid[row][col+1]=2
                    q.append((row,col+1))
            
        return self.minutes if self.count==0 else -1

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    