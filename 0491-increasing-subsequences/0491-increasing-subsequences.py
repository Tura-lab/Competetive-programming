class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        
        path = []
        def dfs(i):
            if len(path) >= 2 and path[-1] < path[-2]:
                return
            
            if len(path) >= 2:
                ans.add(tuple(path[:]))
                
            for j in range(i, n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
                
        dfs(0)
        return ans
        