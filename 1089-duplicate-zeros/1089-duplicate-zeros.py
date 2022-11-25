class Solution:
    def duplicateZeros(self, nums: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        '''
        1 0 0 2 3 0 0 4
        
        '''
        
        zeros = nums.count(0)
        n = len(nums)
        
        for i in range(n-1, -1, -1):
            zeros -= nums[i] == 0
            
            idx = i
            if idx + zeros < n:
                nums[idx + zeros] = nums[i]
                if idx + zeros + 1 < n and nums[i] == 0:
                    nums[idx + zeros + 1] = 0