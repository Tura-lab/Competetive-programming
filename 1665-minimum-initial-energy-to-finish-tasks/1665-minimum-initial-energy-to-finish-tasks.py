class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: (x[1] - x[0], x[1]), reverse = True)
        
        def check(energy):
            for cost, mn in tasks:
                if mn > energy or cost > energy:
                    return False
                energy -= cost
                
            return True
                
        lim = 10 ** 10
        
        l, r = 0, lim
        ans = lim
        while l <= r:
            mid = l  + (r - l) // 2
            
            if check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans
            