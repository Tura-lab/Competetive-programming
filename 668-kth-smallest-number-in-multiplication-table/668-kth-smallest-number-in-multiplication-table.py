class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        ans=0
        def lessthan(mid):
            tot=0
            for i in range(1,m+1):
                tot += min(n, mid//i)
            return tot

        low = 0
        high = m*n
        while low<=high:
            mid = (low+high)//2
            num = lessthan(mid)
            if num < k:
                low = mid+1
            else:
                ans = mid
                high = mid-1
        
        return ans       