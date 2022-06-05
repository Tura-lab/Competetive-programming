class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse = True)
        
        dp = {}
        def solve(total):
            if total == amount:
                return 0
            if total > amount:
                return float('inf')
            
            if total not in dp:
                ans = float('inf')
                
                for coin in coins:
                    ans = min(ans, 1 + solve(total+coin))
                
                dp[total] = ans
            
            return dp[total]
        
        _ans = solve(0)
        return -1 if _ans == float('inf') else _ans
            
            
            
            
            