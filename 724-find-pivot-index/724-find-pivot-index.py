class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        1 7 3  6  5  6
      0 1 8 11 17 22 28
               i
        '''
        pfx_sum = [0]
        for i in range(len(nums)):
            pfx_sum.append(pfx_sum[-1] + nums[i])
        
        for i in range(1,len(pfx_sum)):
            if pfx_sum[i-1] == pfx_sum[-1] - pfx_sum[i]:
                return i-1
        return -1