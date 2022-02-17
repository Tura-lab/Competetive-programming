class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        
        def dfs(cur, total, i):
            if len(cur) == k:
                return ans.append(cur)
            if i>=len(nums):
                return
            
            dfs(cur + [nums[i]], total+nums[i], i+1)
            dfs(cur,total,i+1)
        
        nums = list(range(1,n+1))
        dfs([], 0, 0)
        return ans
    