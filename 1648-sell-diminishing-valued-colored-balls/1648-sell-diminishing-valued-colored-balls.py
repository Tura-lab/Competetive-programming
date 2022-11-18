class Solution:
    def maxProfit(self, nums: List[int], orders: int) -> int:
        mod = 10 **9 +7
        count = 0
        
        nums.append(0)
        nums.sort(reverse = True)
        
        profit = 0
        
        past = None
        for num in nums:
            if past == None or num == past:
                if past == None:
                    past = num
            
            else:
                affordable = count * (past - num)
                
                sell = min(affordable, orders)
                orders -= sell
                
                sold = sell // count
                rem = sell % count
                
                profit += count * (((past) * (past + 1) // 2 )  - ((past-sold) * (past-sold + 1) // 2 ))
                profit += rem * (past - sold)
                
                profit %= mod
                past = num
                                   
            count += 1
                
            if orders == 0:break
                
        return profit
                
                