class Solution:
    '''
    3,0,1
    '''
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while -1 < nums[i] < len(nums) and nums[i] != nums[nums[i]]:
                val = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = val
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return i+1