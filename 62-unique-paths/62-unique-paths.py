class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        cache = {}
        def walker(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i==m and j==n:
                return 1
            down = 0 if i==m else walker(i+1,j)
            right = 0 if j==n else walker(i, j+1)
            
            cache[(i,j)] = down + right
            return cache[(i,j)]

        return walker(1,1)
        