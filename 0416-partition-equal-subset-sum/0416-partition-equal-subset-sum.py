class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total&1:
            print(3434)
            return False
        
        @cache
        def dfs(i, target):
            if i==len(nums):
                return False
            if target == 0:
                return True
            
            return dfs(i+1, target-nums[i]) or dfs(i+1, target)
        
        return dfs(0, total//2)