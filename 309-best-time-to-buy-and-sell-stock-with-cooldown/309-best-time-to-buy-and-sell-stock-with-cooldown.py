class Solution:
    '''
    1  2  3  0  2
    (1,2), (1,3), (0,2)
    1,2
    '''
    def maxProfit(self, prices: List[int]) -> int:
        # print(len(prices))
        
        dp = [[-1 for i in range(len(prices))] for _ in range(len(prices))]
        def dfs(l,r):
            
            if r>=len(prices):
                return 0
            if dp[l][r] !=-1:
                return dp[l][r]
            if prices[l] >= prices[r]:
                return dfs(r,r+1)
            smash = prices[r]-prices[l] + dfs(r+2, r+3)
            passs = dfs(l,r+1)
            
            dp[l][r] = max(smash, passs)
            return dp[l][r]
                    
        return dfs(0,1)