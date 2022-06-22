class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i=2
        j = len(s)//i
        
        while j:
            if s[:j]*i == s:
                return True
            i+=1
            j = len(s)//i
            
        return False
            
            