class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        @cache
        def dfs(i, cur_sign):
            if i == len(nums):
                return 0
            
            # take (respecting the sign) or pass
            
            return max(cur_sign * nums[i] + dfs(i + 1, -1 * cur_sign), dfs(i + 1, cur_sign))
            
            
        return dfs(0, 1)