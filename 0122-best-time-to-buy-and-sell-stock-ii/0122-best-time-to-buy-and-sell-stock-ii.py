class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        cur_hold, cur_not_hold = -float('inf'), 0
        
        for price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            
            cur_hold = max(prev_not_hold - price, prev_hold)
            cur_not_hold = max(prev_hold + price, prev_not_hold)
            
        return cur_not_hold