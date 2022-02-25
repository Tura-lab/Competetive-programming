from math import ceil

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)+1
        ans = 0
        
        while l<=r:
            mid = (l+r)//2
            
            s=0
            for n in nums:
                s += ceil(n/mid)
            
            # print(mid,s)
            if s<=threshold:
                r=mid-1
                ans = mid
            else:
                l=mid+1
                
        return ans