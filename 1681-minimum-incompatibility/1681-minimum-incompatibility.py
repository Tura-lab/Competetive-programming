class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        '''
        (N, 2) ** NUM_SUBSETS
        [6,3,8,1,3,1,2,2]
        [1,1,2,2,3,3,6,8]
        
        '''
        
        n = len(nums)
        per_subset = n // k
        
        @cache
        def dfs(nums):
            if not nums:
                return 0
            
            ans = float('inf')
            for comb in combinations(set(nums), per_subset):
                rem = list(nums)
                for num in comb:
                    rem.remove(num)
                    
                ans = min(ans, max(comb) - min(comb) + dfs(tuple(rem)))
            
            return ans
        
        ans = dfs(tuple(nums))
        return ans if ans < float('inf') else -1