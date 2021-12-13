class Solution:
    def rearrangeArray(self, nums):
        #nums = sorted(nums)
        done = 1
        while True:
            if done == 0:
                break
            done = 0
            for j in range(2, len(nums)):
                if ((nums[j-2] + nums[j])/2) == float(nums[j-1]):
                    nums[j-2], nums[j-1] = nums[j-1], nums[j-2]
                    done=1
        return nums
