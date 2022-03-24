class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            mn = mx = nums[i]
            for j in range(i+1, len(nums)):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
                ans += mx-mn
        return ans