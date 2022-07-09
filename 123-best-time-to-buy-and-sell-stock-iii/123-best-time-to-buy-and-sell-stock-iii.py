class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # print(len(prices))
        
        # The problem is litterally the same as the IVth variant but this time k==2
        
        k = 2
        dp = [[[-1 for _ in range(k)] for __ in range(2)] for ___ in range(len(prices)+1)]
        def solve(i, last, made_yet):
            if i == len(prices) or made_yet==k:
                return 0
            
            # print(i, last, made_yet)
            if dp[i][last][made_yet] == -1:
                
                if last == 0:
                    buy = -prices[i] + solve(i+1, 1, made_yet)
                    dont_buy = solve(i+1, 0, made_yet)
                    dp[i][last][made_yet] = max(buy, dont_buy)
                else:
                    sell = prices[i] + solve(i+1, 0, made_yet+1)
                    dont_sell = solve(i+1, 1, made_yet)
                    dp[i][last][made_yet] = max(sell, dont_sell)

            return dp[i][last][made_yet]
        
        return solve(0, 0, 0)