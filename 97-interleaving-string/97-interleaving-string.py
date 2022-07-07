class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @cache
        def solve(i1, i2):
            if i1+i2 == len(s3) and i2 == len(s2) and i1 == len(s1):
                return True
            
            ans = False
            
            if i1+i2<len(s3) and i1<len(s1) and s3[i1+i2] == s1[i1]:
                ans = ans or solve(i1+1, i2)
            
            if i1+i2<len(s3) and i2<len(s2) and s3[i1+i2] == s2[i2]:
                ans = ans or solve(i1, i2+1)
            
            return ans
        
        return solve(0,0)