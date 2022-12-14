class Solution:
    '''
    1 2 3 1
    
    '''
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        
        a, b, c, d, ans = 0, nums[0], nums[1], 0, 0
        for i in range(2, n):
            d = nums[i] + max(a, b)
            ans = max(a,b,c,d,ans)
            a = b
            b = c
            c = d
        
        return ans
        
        