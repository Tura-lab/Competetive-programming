class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        ans = 0
        
        while l<=r:
            mid = (l+r)//2
            
            cur = 0
            d=1
            for w in weights:
                if cur+w<=mid:
                    cur+=w
                else:
                    cur = w
                    d+=1
            
            if d<=days:
                ans = mid
                r=mid-1
            else:
                l=mid+1
                
        return ans