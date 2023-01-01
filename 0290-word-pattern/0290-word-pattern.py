class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        found = {}
        found2 = {}
        s = s.split()
        
        i, j = 0, 0
        while i < len(pattern) or j < len(s):
            if i == len(pattern) or j == len(s):
                return False
            
            if (s[j] in found2 and found2[s[j]] != pattern[i]) or (pattern[i] in found and found[pattern[i]] != s[j]):
                return False
            
            found[pattern[i]] = s[j]
            found2[s[j]] = pattern[i]
            
            i += 1
            j += 1
            
        return True