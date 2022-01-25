class Solution:
    '''
    0 1 2 3 4 2 3 3 4
                    i
            j
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        j=0
        i=1
        while i <len(nums):
            if nums[i] != nums[j]:
                j+=1
                nums[j] = nums[i]
            i+=1
            
        return j+1