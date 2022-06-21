class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s = list(s)
        for i in range(len((s))):
            if s[i]==c:
                s[i] = 0
            else:
                s[i] = float(inf)
            
        found = None
        for i in range(len(s)):
            if s[i] == 0:
                found = i
            if found!=None:
                s[i] = min(s[i], abs(i-found))
        
        found = None
        for i in range(len(s)-1, -1, -1):
            if s[i] == 0:
                found = i
            if found:
                s[i] = min(s[i], abs(i-found))
                                
        return s