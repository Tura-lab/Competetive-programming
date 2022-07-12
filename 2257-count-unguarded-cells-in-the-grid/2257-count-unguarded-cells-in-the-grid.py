class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        
        graph = [['']*n for _ in range(m)]
        
        for r,c in guards:
            graph[r][c] = 'G'
            
        for r,c in walls:
            graph[r][c] = 'W'
            
            
        # print(graph)
        visited = set()
        def dfs(row, col, past):
            if not(-1<row<m and -1<col<n) or graph[row][col]=='W':
                return
            if graph[row][col] == 'G' and (row,col)in visited:
                return
            
            visited.add((row, col))
            
            if (graph[row][col]=='G' or past=='up') and past!='down':
                dfs(row-1, col, 'up')
            if (graph[row][col]=='G' or past=='down') and past!='up':
                dfs(row+1, col, 'down')
            if (graph[row][col]=='G' or past=='left') and past!='right':
                dfs(row, col-1, 'left')
            if (graph[row][col]=='G' or past=='right') and past!='left':
                dfs(row, col+1, 'right')
            
            
        for i in range(m):
            for j in range(n):
                if graph[i][j]=='G' and (i,j) not in visited:
                    dfs(i, j, 'all')
            
        # print(visited)
        return m*n - len(visited) - len(walls)
