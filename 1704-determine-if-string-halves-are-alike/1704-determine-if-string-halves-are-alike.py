class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def counter(s):
            count = 0
            for l in s:
                count += l in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
                    
            return count
        
        n = len(s)
        return counter(s[:n//2]) == counter(s[n//2:])