class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        '''
        Input: nums = [3,6,5,1,8]
        
        '''
        dp = [0, 0, 0]
        
        for num in nums:
            cur = num % 3
            for n in dp[:]:
                dp[(n+num)%3] = max(dp[(n+num)%3], num+n)
                    
        return dp[0]