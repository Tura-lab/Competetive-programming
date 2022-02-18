class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        [2,3,-2,4]
        max =  6
        min =  2
        '''
        max_yet = low = high = nums[0]
        for i in range(1, len(nums)):
            
            if nums[i]<0:
                high, low = low, high
                
            high = max(nums[i], high*nums[i])
            low  = min(nums[i], low*nums[i])
            
            max_yet = max(max_yet, high)
            
        return max_yet