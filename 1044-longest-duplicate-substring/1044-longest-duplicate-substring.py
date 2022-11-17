class Solution:
    def longestDupSubstring(self, s: str) -> str:
        string = [0, -1]
        
        def f(l):
            return ord(l) - ord('a') + 1
        
        def check(size):
            found = set()
            code = 0
            p, mod = 31, 2**63 -1
        
            for i in range(size):
                code = (code * p + f(s[i])) % mod
                
            power = pow(p, size, mod)
            
            found.add(code)
            i = 0
            for j in range(size, len(s)):
                code = (code * p + f(s[j]) - f(s[i]) * power) % mod
                i+=1
                
                if code in found:
                    string[0] = i
                    string[1] = j
                    return True
                found.add(code)
            return False
            
        
        ans = 0
        l, r = 1, len(s)-1
        while l <= r:
            mid = l + (r-l)//2
            
            if check(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        l,r = string[0], string[1]+1
        return s[l:r]