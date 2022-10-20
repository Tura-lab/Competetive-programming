class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = list(set(coins))
        coins.sort(reverse=True)
        
        @cache
        def dfs(i, amount):
            if amount == 0:
                return 0
            if amount < 0 or i==len(coins):
                return float('inf')
            
            take = 1 + dfs(i, amount-coins[i])
            dont = dfs(i+1, amount)
        
            return min(take, dont)
        
        ans = dfs(0, amount)
        return -1 if ans == float('inf') else ans