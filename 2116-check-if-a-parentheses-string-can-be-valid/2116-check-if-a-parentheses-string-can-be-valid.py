class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            return False
        
        count = 0
        for i in range(len(s)):
            if s[i] == '(' or locked[i] == '0':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                return False
            
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')' or locked[i] == '0':
                count += 1
            else:
                count -= 1
            
            if count < 0:
                return False
            
        return True