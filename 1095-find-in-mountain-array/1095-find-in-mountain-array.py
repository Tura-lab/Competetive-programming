# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        
        l, r = 0, n-1
        
        peak = None
        while l <= r:
            mid = l + (r-l) // 2
            
            if mid == 0 or mid == n-1:
                if mid == 0:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            else:
                left, cur, right = mountain_arr.get(mid-1), mountain_arr.get(mid), mountain_arr.get(mid+1)
                
                if left < cur and cur > right:
                    peak = mid
                    break
                elif left < cur:
                    l = mid + 1
                else:
                    r = mid - 1
                    
        
        # search left
        l, r = 0, peak
        
        while l <= r:
            mid = l + (r-l) // 2
            
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
                
        
        # search right
        l, r = peak, n-1
        
        while l <= r:
            mid = l + (r-l) // 2
            
            cur = mountain_arr.get(mid)
            if cur == target:
                return mid
            
            elif cur < target:
                r = mid - 1
            else:
                l = mid + 1
                
        
        
        
        
        return -1