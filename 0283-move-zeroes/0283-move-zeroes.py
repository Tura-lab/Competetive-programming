class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1 3 0 0 12
            i
                 j
        '''
        i = 0 # points to a zero
        j = 0 # points to a nonzero
        
        while j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            
            while j < len(nums) and (j <= i or nums[j] == 0):
                j += 1
                
            if i == len(nums) or j == len(nums):break
            nums[i], nums[j] = nums[j], nums[i]