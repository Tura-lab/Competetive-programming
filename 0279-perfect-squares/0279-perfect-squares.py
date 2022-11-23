class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        
        for i in range(1, int(sqrt(n)+1)):
            perfect_squares.append(i*i)
        
        q = deque([0])
        visited = set([0])
        
        steps = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                for num in perfect_squares:
                    cur = num + node
                    
                    if cur == n:
                        return steps
                    
                    if cur < n and cur not in visited:
                        visited.add(cur)
                        q.append(cur)
            steps += 1
        