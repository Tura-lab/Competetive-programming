from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(i, tot):
            if i==len(nums):
                if tot == target:
                    return 1
                return 0
            
            return dfs(i+1, tot-nums[i]) + dfs(i+1, tot+nums[i])
        
        return dfs(0,0)