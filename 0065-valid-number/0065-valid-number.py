class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        
        count = 0
        for l in s:
            count += not l.isdigit() and l not in ('.', '+', '-')
            if count > 1:
                return False
        
        if 'e' not in s:
            try:
                float(s)
                return s
            except:
                return False
        
        idx = s.index('e')
        left, right = s[:idx], s[idx+1:]
        
        if not left or not right:
            return False
        
        try:
            float(left)
            int(right)
            return True
        except:
            return False
        