class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n   = len(nums)
        mod = 10 ** 9 + 7
        left, right = [0] * n, [len(nums)-1] * n
        
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1][0] > nums[i]:
                num, idx = stack.pop()
                right[idx] = i-1
            stack.append((nums[i], i))
                    
        stack = []
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1][0] > nums[i]:
                num, idx = stack.pop()
                left[idx] = i+1
            stack.append((nums[i], i))
        
        p_sum = [0]
        for num in nums:
            p_sum.append(num+p_sum[-1])
        
        ans = float('-inf')
        for i in range(len(nums)):
            ans = max(ans, nums[i] * (p_sum[right[i]+1] - p_sum[left[i]]))
        
        return ans % mod
        
        
        