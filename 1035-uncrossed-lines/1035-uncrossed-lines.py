from collections import deque

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        d = defaultdict(deque)
        for i in range(len(nums2)):
            d[nums2[i]].append(i)
            
        @cache
        def dfs(i, last_j):
            if i==len(nums1):
                return 0
            
            best = 0
            idx = 0
            if nums1[i] not in d:
                return dfs(i+1, last_j)
            
            while idx < len(d[nums1[i]]) and d[nums1[i]][idx] <= last_j:
                idx +=1
            
            if idx < len(d[nums1[i]]):
                return max(1 + dfs(i+1, d[nums1[i]][idx]), dfs(i+1, last_j))
            
            return dfs(i+1, last_j)
    
        return dfs(0, -1)