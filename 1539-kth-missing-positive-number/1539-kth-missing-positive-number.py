class Solution:
    def findKthPositive(self, nums: List[int], k: int) -> int:
        '''
        2 3 4 7 11
        
        
        '''
        
        ans = -1
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if nums[mid] - mid - 1 < k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        if ans == -1:
            return k
        
        k -= nums[ans] - ans - 1
        
        return nums[ans] + k 
                