class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        abcbka
        
        "ececabbacec"
        '''
        count = 0
        
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i] != s[j]:
                if count == 1:
                    return False
                
                if s[i] == s[j-1] and s[i+1] == s[j]:
                    pass
                elif s[i] == s[j-1]:
                    i -= 1
                    count += 1
                elif s[i+1] == s[j]:
                    j += 1
                    count += 1
                else:
                    return False
                
                
            i += 1
            j -= 1
            
        return True