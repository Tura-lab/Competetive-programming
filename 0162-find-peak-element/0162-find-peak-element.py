class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if (i - 1 < 0 or nums[i] > nums[i - 1]) and (i + 1 >= len(nums) or nums[i] > nums[i + 1]):
                return i