class Solution:
    def strStr(self, h: str, n: str) -> int:
        if not n:
            return 0
        if len(n) > len(h):
            return -1
        
        def valid(i,j):
            k=0
            while i<j and k<len(n):
                if h[i] != n[k]:
                    return False
                i+=1
                k+=1
            return True
        
        i = 0
        j=len(n)
        
        if valid(i,j):
            return i
        while j<len(h):
            i+=1
            j+=1
            if valid(i,j):
                return i
            
        return -1