class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 0
        
        for rod in rods:
            new_dp = dp.copy()
            for dif in dp:
                tall = dp[dif]
                short = tall - dif
                
                # add it to short
                new_tall, new_short = max(tall, short + rod), min(tall, short + rod)
                val = new_dp[new_tall - new_short] if new_tall - new_short in new_dp else 0
                new_dp[new_tall - new_short] = max(val, new_tall)
        
                # add it to tall
                new_tall, new_short = max(tall + rod, short), min(tall + rod, short)
                val = new_dp[new_tall - new_short] if new_tall - new_short in new_dp else 0
                new_dp[new_tall - new_short] = max(val, new_tall)
            
            dp = new_dp
            
        return dp[0]