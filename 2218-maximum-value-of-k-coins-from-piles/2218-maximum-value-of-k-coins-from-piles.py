class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        for pile in piles:
            for i in range(1, len(pile)):
                pile[i] += pile[i-1]
        
        @cache
        def dfs(i, taken):
            if i == len(piles) or taken == 0:
                return 0
            if taken < 0:
                return -float('inf')
            
            maximum = dfs(i+1, taken)
            for j in range(min(taken, len(piles[i]))):
                maximum = max(maximum, piles[i][j] + dfs(i+1, taken-(j+1)))
                
            return maximum
        
        return dfs(0, k)