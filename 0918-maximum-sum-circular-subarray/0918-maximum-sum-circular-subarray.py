class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ans = -float('inf')
        mx = -float('inf')
        for i in range(len(nums)):
            mx = max(mx + nums[i], nums[i])
            ans = max(ans, mx)
            
        p_sum = [nums[0]]
        for i, num in enumerate(nums[1:]):
            p_sum.append(p_sum[-1] + num)
            
        s_sum = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            s_sum.append(s_sum[-1] + nums[i])
            
        s_sum = s_sum[::-1]
        for i in range(len(s_sum) - 2, -1, -1):
            s_sum[i] = max(s_sum[i], s_sum[i + 1])
            
        cur_best = p_sum[0]
        for i in range(1, len(p_sum) - 1):
            # print(i, cur_best, s_sum[i + 1])
            ans = max(ans, cur_best + s_sum[i + 1])
            cur_best = max(cur_best, p_sum[i])
            
            
        return ans