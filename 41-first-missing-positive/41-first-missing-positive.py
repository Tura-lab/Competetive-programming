class Solution:
    '''
    -1 1 3 4
     0 1 2
       
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
                
        missing = 1
        for j in range(i, len(nums)):
            if nums[j]>missing:
                return missing
            if nums[j] == missing:
                missing = nums[j]+1
        
        return missing
        