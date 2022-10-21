class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        path = []
        def dfs(i):
            if i == n:
                if len(path)>1:
                    ans.add(tuple(path))
                return 
            
            if not path or path[-1] <= nums[i]:
                path.append(nums[i])
                dfs(i+1)
                path.pop()
            dfs(i+1)
            
        dfs(0)
        return ans