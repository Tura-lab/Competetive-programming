class Solution:
    def reverseVowels(self, s: str) -> str:
        i, j = 0, len(s)-1
        s = list(s)
        
        while i<j:
            while -1<i<len(s) and s[i] not in 'aeiouAEIOU':
                i+=1
            while -1<j<len(s) and s[j] not in 'aeiouAEIOU':
                j-=1
            
            if not i<j:break
            
            s[i], s[j] = s[j], s[i]
            
            i+=1
            j-=1
            
        return ''.join(s)