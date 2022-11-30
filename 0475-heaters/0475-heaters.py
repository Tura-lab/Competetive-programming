class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()
        '''
        he => heaters
        ho => houses
        
        
        '''
        
        def check(rad):
            j = 0
            for i, heater in enumerate(heaters):
                while j < len(houses) and heater - rad <= houses[j] <= heater + rad:
                    j += 1
            
            return j == len(houses)
                    
        
        l, r = 0, 10**9
        
        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans