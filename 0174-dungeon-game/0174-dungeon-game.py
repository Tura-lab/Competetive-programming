class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        directions = [(0,1), (1,0)]

        def in_bound(row, col):
            return -1<row<rows and -1<col<cols

        @cache
        def dfs(row, col):
            if not in_bound(row, col):
                return float('inf')
            if (row, col) == (rows-1, cols-1):
                return max(0, -dungeon[row][col])
            
            ans = -dungeon[row][col] + min(dfs(row+1, col), dfs(row, col+1))

            return max(0, ans)

        return dfs(0,0) + 1