class Solution:
    '''
    1 2 3 1
    
    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n+3)
        
        for i in range(3, n+3):
            dp[i] = nums[i-3] + max(dp[i-2], dp[i-3])
            
        return max(dp)
        
        