class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums = [1] + nums + [1]
        
        # depth = []
        
        @cache
        def dfs(left, right):
            if right - left < 2:return 0
            
            ans = 0
            
            for cur in range(left+1, right):
                ans = max(ans, nums[left] * nums[right] * nums[cur] + dfs(left, cur) + dfs(cur, right))    
                
            return ans
        
        return dfs(0, n+1)