class Solution:
    def minimumWhiteTiles(self, nums: str, numCarpets: int, carpetLen: int) -> int:
        @cache
        def dfs(i, rem):
            return 0 if i >= len(nums) else min((1 if nums[i]=='1' else 0) + dfs(i+1, rem), dfs(i+carpetLen, rem-1) if rem and nums[i]=='1' else float('inf'))
        
        return dfs(0, numCarpets)