class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]
        
        def in_bound(row,col):
            return -1<row<rows and -1<col<cols
        
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append((i,j))
                    mat[i][j] = 2
        
        steps = 0
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                
                dist[row][col] = steps
                
                for x, y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nx, ny = row+x, col+y
                    
                    if in_bound(nx,ny) and mat[nx][ny] != 2:
                        q.append((nx,ny))
                        mat[nx][ny] = 2
            steps += 1
            
        return dist