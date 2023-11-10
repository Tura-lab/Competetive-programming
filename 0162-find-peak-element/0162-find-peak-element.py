class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        1, 2, 1, 3, 5, 6, 4
        
        """
        n = len(nums)
        
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (mid + 1 == n or nums[mid] > nums[mid + 1]):
                return mid 
            
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (mid + 1 == n or nums[mid] < nums[mid + 1]):
                l = mid + 1
            else:
                r = mid - 1 
                
        