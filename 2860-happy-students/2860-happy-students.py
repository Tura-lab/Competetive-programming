class Solution:
    def countWays(self, nums: List[int]) -> int:
        """
        [1,1]
        
        """
        nums.sort()
        next_greater = [0] * len(nums)
        past = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            next_greater[i] = past
            if i > 0 and nums[i - 1] != nums[i]:
                past = nums[i]

        
        ans = 0 not in nums
        for i, num in enumerate(nums):
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                continue
            
            if num <= i and next_greater[i] > i + 1:
                ans += 1
            
        return ans