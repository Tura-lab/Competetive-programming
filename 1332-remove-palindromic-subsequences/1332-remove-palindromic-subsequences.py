class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPal(s):
            i = 0
            j = len(s)-1
            while i<=j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
                
            return True
        
        return 1 if isPal(s) else 2