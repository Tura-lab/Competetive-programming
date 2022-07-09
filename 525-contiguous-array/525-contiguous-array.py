class Solution:
    '''
       0 1  0  0  1
    0 -1 0 -1 -2 -1
    '''
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        found = {0:-1}
        
        for i in range(len(nums)):
            num = nums[i]
            count += -1 if num==0 else 1
            
            if count in found:
                ans = max(ans, i-found[count])
            else:
                found[count] = i
        
        return ans
        