class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
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
        
        mx = -float('inf')
        for i in range(n):
            l, r = left[i], right[i]
            if l <= k <= r:
                mx = max(mx, (r - l + 1) * nums[i])
        
        return mx