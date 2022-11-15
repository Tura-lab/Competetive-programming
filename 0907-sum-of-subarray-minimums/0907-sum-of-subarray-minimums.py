class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        n = len(nums)
        mod = 10**9 +7
        
        left  = [0] * n
        right = [n-1] * n
        
        stack = []
        for i in range(n):
            while stack and stack[-1][0] > nums[i]:
                num, idx = stack.pop()
                right[idx] = i-1
            stack.append((nums[i], i))
            
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= nums[i]:
                num, idx = stack.pop()
                left[idx] = i+1
            stack.append((nums[i], i))
            
        count = 0
        for i in range(n):
            count += (i - left[i] + 1) * (right[i] - i + 1) * nums[i]
            count %= mod

        return count