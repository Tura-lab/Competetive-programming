class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        total, n = sum(nums), len(nums)
        
        if total == 0:
            return n > 1
        
        @cache
        def dfs(i, size, target_sum):
            if size < 0 or target_sum < 0:
                return False
            
            if i == n:return target_sum == size == 0
            
            return dfs(i+1, size-1, target_sum - nums[i]) or dfs(i+1, size, target_sum)
        
        
        for size in range(1, n):
            if (total * size) % n == 0:
                if dfs(0, size, (total * size) // n):
                    return True
            
        return False