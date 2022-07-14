class Solution:
    '''
     1  2  3 4
     1 -1  3 4
    '''
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while -1<nums[i]-1<len(nums) and i!=nums[i]-1 and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                
        # print(nums)
        
        ans = 1
        for num in nums:
            if num != ans:
                return ans
            ans+=1
        
        return ans