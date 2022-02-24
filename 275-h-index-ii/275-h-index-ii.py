class Solution:
    '''
    1 2 3 4 5 6
    
    '''
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l=0
        r=len(citations)
        ans = 0
        
        while l<=r:
            h = (l+r)//2
            if h==0 or h <= citations[n-h]:
                print(h, citations[n-h if h!=0 else n-1], 258954)
                ans = h
                l = h+1
            else:
                r = h-1                
        return ans