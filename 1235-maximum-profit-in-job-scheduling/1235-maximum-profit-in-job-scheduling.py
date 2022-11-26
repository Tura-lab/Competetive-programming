class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        '''
         1,  2,  3,  3 => startTime
         3,  4,  5,  6 => endTime
        50, 10, 40, 70 => profit
         0  10  40   70           
        120 70  70   70
        '''
        nums = sorted(list(zip(startTime, endTime, profit)))
        
        n = len(nums)
        dp = [0] * n
        
        dp[-1] = nums[-1][-1]
        mx = nums[-1][-1]
        
        for i in range(n-2, -1, -1):
            start, end, profit = nums[i]
            l, r = i+1, n-1
            ans = -1
            
            while l <= r:
                mid = l + (r - l) // 2
                
                if nums[mid][0] >= end:
                    ans = mid
                    r = mid - 1
                else:
                    l = mid + 1
            
            if ans == -1:
                dp[i] = profit
            else:
                dp[i] = profit + dp[ans]
            
            mx = max(mx, dp[i])
            dp[i] = mx
                
        # print(dp)
        # print(maxs)
        return max(dp)
        