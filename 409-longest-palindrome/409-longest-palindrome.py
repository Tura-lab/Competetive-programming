class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = {}
        for c in s:
            if c not in counts:
                counts[c] =1
            else:
                counts[c]+=1
            
        doubles = 0
        
        for i,j in counts.items():
            doubles += j>>1
        
        ans = doubles *2
        if ans < len(s):
            ans += 1
        
        return ans