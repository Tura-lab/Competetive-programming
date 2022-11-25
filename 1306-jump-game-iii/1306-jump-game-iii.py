class Solution:
    def canReach(self, nums: List[int], start: int) -> bool:
        n = len(nums)
        
        @cache
        def dfs(i):
            if not 0 <= i < n:
                return False
            if nums[i] == 0:
                return True
            if nums[i] < 0:
                return False
            
            nums[i] *= -1
            
            ans = dfs(i + nums[i]) or dfs(i - nums[i])
            
            nums[i] *= -1
            
            return ans
        
        return dfs(start)