class Solution:
    '''
    6  3  2
    1  2  3  4
  0 1  2  6  24  
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_sum = [1]
        for num in nums:
            pre_sum.append(pre_sum[-1]*num) 
        ans = [0]*len(nums)
        mul=1
        for i in range(len(nums)-1, -1, -1):
            ans[i] = pre_sum[i]*mul
            mul*=nums[i]
        return ans