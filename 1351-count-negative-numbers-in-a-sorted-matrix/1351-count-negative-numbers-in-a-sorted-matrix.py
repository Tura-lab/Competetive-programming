class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in grid:
            l=0
            r=len(row)
            if row[0]<0:
                ans += len(row)
                continue
            if row[-1]>=0:
                continue
            while l<=r:
                mid = (l+r)//2
                if mid-1>-1 and row[mid]<0 and row[mid-1]>=0:
                    ans += len(row) - mid
                    print(len(row) - mid)
                    break
                elif row[mid]<0:
                    r = mid-1
                else:
                    l = mid+1
                
        return ans
                    