class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
    
        def in_bound(row, col):
            return 0<=row<n and 0<=col<n

        queue = deque()
        visited = set()

        n = len(grid)

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    queue.append((row,col))
                    visited.add((row,col))

        if len(queue) == 0:
            return -1
        if len(queue) == n*n:
            return -1

        distance = 0
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()

                if grid[row][col] == 0:
                    distance = max(distance, steps)

                for x,y in [[1,0],[0,1],[-1,0],[0,-1]]:
                    newx, newy = row + x, col + y
                    if in_bound(newx, newy) and (newx, newy) not in visited:
                        visited.add((newx, newy))
                        queue.append((newx, newy))
            steps += 1

        return distance