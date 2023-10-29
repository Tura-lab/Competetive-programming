class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        backs = backt = 0
        i,j = len(s) - 1, len(t) - 1
        
        while i >= 0 and j >= 0:
            if i >= 0 and j >= 0 and s[i] != '#' and t[j] != '#':
                if s[i] != t[j]:
                    return False
                i -= 1
                j -= 1
            
            while i >= 0 and s[i] == '#':
                i -= 1
                backs += 1
                
            while j >= 0 and t[j] == '#':
                j -= 1
                backt += 1    
            
            while i >= 0 and backs:
                if s[i] != '#':
                    backs -= 1
                else:
                    backs += 1
                i -= 1
            
            while j >= 0 and backt:
                if t[j] != '#':
                    backt -= 1
                else:
                    backt += 1
                j -= 1
                
        while i >= 0:
            if s[i] != '#':
                return False
            
            while i >= 0 and s[i] == '#':
                i -= 1
                backs += 1
            
            while i >= 0 and backs:
                if s[i] != '#':
                    backs -= 1
                else:
                    backs += 1
                i -= 1
                
            
        while j >= 0:
            if t[j] != '#':
                return False
            
            while j >= 0 and t[j] == '#':
                j -= 1
                backt += 1
            
            while j >= 0 and backt:
                if t[j] != '#':
                    backt -= 1
                else:
                    backt += 1
                j -= 1
        
        return True