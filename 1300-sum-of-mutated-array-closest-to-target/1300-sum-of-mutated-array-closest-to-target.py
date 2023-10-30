class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        tot = sum(arr)
        arr.sort()
        p_sum = [0] + list(accumulate(arr))
        
        def check(num):
            bigger_count = len(arr) - bisect_left(arr, num)
            
            return tot if bigger_count == 0 else tot - (p_sum[-1] - p_sum[len(arr) - bigger_count]) + (bigger_count * num)
        
        
        l,r = 0, arr[-1]
        best = float('inf')
        ans = arr[-1]
        
        while l <= r:
            mid = l + (r - l) // 2
            
            val = check(mid) - target
            
            if abs(val) < best:
                best = abs(val)
                ans = mid
            elif abs(val) == best:
                ans = min(ans, mid)
                
            
            if val > 0:
                r = mid - 1
            else:
                l = mid + 1
                
        return ans