class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, 10000):
            cur_sum = 0
            idx = i
            cur_num = 1
            while idx <= len(nums):
                cur_sum += nums[idx-1]
                cur_num += 1
                idx = i * cur_num * cur_num
                
            ans = max(ans, cur_sum)
            
        return ans