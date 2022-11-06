class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k&1:
            return -1
        if k == len(nums):
            return max(nums[:-1])
        if k > len(nums):
            return max(nums)
        if k == 0 or k==1:
            return nums[k]

        return max(max(nums[:k-1]), nums[k])