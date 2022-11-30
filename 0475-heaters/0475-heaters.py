class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        
        def check(rad):
            ranges = []
            for h in heaters:
                ranges.append((h - rad, h + rad))
            
            for house in houses:
                l2, r2 = 0, len(ranges)-1
                found = False
                
                while l2<=r2:
                    mid2 = l2 + (r2 - l2) // 2
                    
                    if ranges[mid2][0] > house:
                        r2 = mid2 - 1
                    elif ranges[mid2][1] < house:
                        l2 = mid2 + 1
                    else:
                        found = True
                        break
                
                if not found: return False
                
            return True
            
        
        l, r = 0, 10**10
        
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans