class Solution:
    def change(self, amount: int, nums: List[int]) -> int:
        nums.sort(reverse=True)
        @cache
        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            
            count = 0
            for j in range(i, len(nums)):
                count += dfs(j, amount-nums[j])
                
            return count
        
        return dfs(0, amount)