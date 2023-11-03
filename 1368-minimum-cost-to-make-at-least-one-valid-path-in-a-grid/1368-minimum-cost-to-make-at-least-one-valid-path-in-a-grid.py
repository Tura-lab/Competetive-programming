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
        
        heap = []
        heappush(heap, (0, (0, 0)))
        
        distances = defaultdict()
        while heap:
            cost, node = heappop(heap)
            if node not in distances:
                distances[node] = cost
                for x, y in [[1,0], [0, 1], [0, -1], [-1, 0]]:
                    v = (x + node[0], y + node[1])
                    w = get_sign(x, y) != grid[node[0]][node[1]]
                    if in_bound(v[0], v[1]) and v not in distances:
                        heappush(heap, (cost + w, v))


        return distances[(rows - 1, cols - 1)]
            
            