from functools import lru_cache

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        20  40  20  70  30
        50  20  50  40  20
        '''
        def dfs(i, turn, swapped):
            if i == n:
                return 0
            
            if (i, turn, swapped) not in memo:
                
                ans = nums[turn][i] + dfs(i+1, turn, swapped)
                
                if not swapped:
                    ans = max(ans, nums[1][i] + dfs(i+1, 1, True))
                if swapped and turn == 1:
                    ans = max(ans, nums[0][i] + dfs(i+1, 0, swapped))
            
                memo[(i, turn, swapped)] = ans
            
            return memo[(i, turn, swapped)]
        
        nums = [nums1, nums2]
        n = len(nums1)
        
        memo = {}
        first = dfs(0, 0, False)
        nums[0], nums[1] = nums[1], nums[0]
        
        memo = {}
        
        return max(first, dfs(0, 0, False))