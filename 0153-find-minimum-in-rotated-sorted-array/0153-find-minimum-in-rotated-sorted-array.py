class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find the smallest
        left_most = nums[0]
        l, r = 1, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            
            if left_most < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
            
        return nums[0] if l == len(nums) else nums[l]