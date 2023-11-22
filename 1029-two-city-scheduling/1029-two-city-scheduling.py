class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        @cache
        def dfs(i, count):
            if count > n // 2:
                return float('inf')
            if i == n:
                return 0 if count == n // 2 else float('inf')
            
            return min(costs[i][0] + dfs(i + 1, count + 1), costs[i][1] + dfs(i + 1, count))
        
        return dfs(0, 0)