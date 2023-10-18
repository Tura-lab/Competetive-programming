class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        
        @cache
        def dfs(i, holding_stock):
            if i == n:
                return 0 if not holding_stock else -float('inf')
            
            if holding_stock:
                return max(dfs(i + 1, holding_stock), dfs(i + 1, False) + prices[i])
            
            return max(dfs(i + 1, False), dfs(i + 1, True) - prices[i])
        
        return dfs(0, False)