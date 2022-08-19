class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = last = -1
        
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] >= target:
                r= mid-1
                if nums[mid] == target:
                    first = mid
            else:
                l=mid+1
        
        l=0
        r=len(nums)-1
        
        while l<=r:
            mid = (l+r)//2
            
            if nums[mid] <= target:
                l= mid+1
                if nums[mid] == target:
                    last = mid
            else:
                r=mid-1
        
        return  [first,last]