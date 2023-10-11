class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        0,0,0,1,1,1,1,2,3,3
          i
            j
        '''
        duplicate_count = 0
        cur = None
        cur_count = 0
        
        i = 0
        for j in range(len(nums)):
            
            if nums[j] == cur:
                cur_count += 1
            else:
                cur = nums[j]
                cur_count = 1
                
            nums[i], nums[j] = nums[j], nums[i]
            
            if cur_count <= 2:
                i += 1
                
        return i