class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[1,0], [0,1], [0,-1],[-1,0]]
        r,c = len(matrix), len(matrix[0])
        
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for i in range(r):
            for j in range(c):
                for x,y in directions:
                    nx,ny = x+i, y+j
                    if -1<nx<r and -1<ny<c and matrix[nx][ny] > matrix[i][j]:
                        graph[(i,j)].append((nx,ny))
                        indeg[(nx,ny)] += 1
                        
        q = deque()
        for i in range(r):
            for j in range(c):
                if indeg[(i,j)] == 0:
                    q.append((i,j))
                
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                
                for v in graph[node]:
                    indeg[v] -=1
                    if indeg[v] == 0:
                        q.append(v)
            count +=1
        return count