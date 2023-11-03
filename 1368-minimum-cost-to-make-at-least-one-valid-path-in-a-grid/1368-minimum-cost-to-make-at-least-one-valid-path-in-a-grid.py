class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        def get_sign(i, j):
            if i == 1 and j == 0:
                return 3
            if i == 0 and j == 1:
                return 1
            if i == -1 and j == 0:
                return 4
            else:
                return 2
            
        rows, cols = len(grid), len(grid[0])
        def in_bound(row, col):
            return -1 < row < rows and -1 < col < cols
        
        graph = defaultdict(list)
        for i in range(rows):
            for j in range(cols):
                for x,y in [[1,0], [0, 1], [0, -1], [-1, 0]]:
                    nx, ny = i + x, j + y
                    if in_bound(nx, ny):
                        graph[(i, j)].append(((nx, ny), 0 if get_sign(x, y) == grid[i][j] else 1))
                        
        
        heap = []
        heappush(heap, (0, (0, 0)))
        
        distances = defaultdict()
        while heap:
            cost, node = heappop(heap)
            if node not in distances:
                distances[node] = cost
                for v, w in graph[node]:
                    if v not in distances:
                        heappush(heap, (cost + w, v))


        return distances[(rows - 1, cols - 1)]
            
            