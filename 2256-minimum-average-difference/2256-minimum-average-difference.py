class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i-1]
            
        ans = float('inf')
        
        idx = 0
        for i in range(n):
            left = nums[i] // (i+1)
            right = 0 if i == n-1 else (nums[-1] - nums[i]) // (n-i-1)
            cur =  abs(left - right)
            
            if cur < ans:
                ans = cur
                idx = i
            
        return idx
            