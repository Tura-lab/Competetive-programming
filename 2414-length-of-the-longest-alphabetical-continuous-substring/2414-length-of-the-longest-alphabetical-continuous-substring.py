class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans, n = 1, len(s)
        count = 1
        
        for i in range(1, n):
            if ord(s[i]) - ord(s[i-1]) == 1:
                count += 1
            else:
                count = 1
            
            ans = max(ans, count)
    
    
        return max(ans, count)
    