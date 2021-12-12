class Solution:
    def largestNumber(self, nums):
        ans=''
        nums = sorted([str(n) for n in nums], reverse=True)
        for i in range(len(nums)-1):
            j=i
            while int(ans+str(nums[j])+str(nums[j+1])) < int(ans+str(nums[j+1])+str(nums[j])) and j>-1:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                j-=1
        if int(''.join(nums)) == 0:
            return str(0)
        return ''.join(nums)
