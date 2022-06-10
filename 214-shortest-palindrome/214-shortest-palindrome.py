'''
kada
adak
'''
class Solution:
    
    def shortestPalindrome(self, s: str) -> str:
        def h(l):
            return ord(l)-ord('a')+1
        
        mod = 10**9 +7
        l_hash = r_hash = 0
        ans = 1
        
        p=1
        for i in range(len(s)):
            l_hash = (l_hash + (h(s[i]) * p)%mod)%mod
            r_hash = (r_hash * 26)%mod
            r_hash = (r_hash + h(s[i]))%mod
            
            i+=1            
            if l_hash == r_hash:
                ans = i
            
            p = (p * 26)%mod
            
        # print(ans)
        return s[ans:][::-1] + s
            
        
        