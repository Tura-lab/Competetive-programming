class Solution:
    def totalStrength(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        left_max = [0]*len(nums)
        right_max = [len(nums)-1]*len(nums)
        
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] <= stack[-1][0]:
                _, idx = stack.pop()
                right_max[idx] = i-1
            stack.append((nums[i], i))
        
        stack = []
        for i in range(len(nums)-1, -1,-1):
            while stack and nums[i] < stack[-1][0]:
                _,idx = stack.pop()
                left_max[idx] = i+1
            stack.append((nums[i], i))
        
        p_sum = list(accumulate(accumulate(nums), initial = 0))
        
        ans = 0
        for i in range(len(nums)):
            l, r = left_max[i], right_max[i]
            
            lef = p_sum[i] - p_sum[max(0, l-1)]
            rig = p_sum[r+1] - p_sum[i]
            
            l, r = i-l+1, r-i+1
            
            ans += nums[i] * (rig * l - lef * r)
            ans %= mod
        
        return ans