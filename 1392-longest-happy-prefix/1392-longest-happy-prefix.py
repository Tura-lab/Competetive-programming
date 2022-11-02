class Solution:
    def longestPrefix(self, s: str) -> str:
        # print(len(s))
        p = 29
        mod = 10**9 +7
        
        def h(l):
            return ord(l) - ord('a') + 1
        
        pre_hash = suf_hash = 0
        j = len(s)-1
        ans = -1
        for i in range(len(s)-1):
            pre_hash += h(s[i]) * pow(p,i,mod)
            
            suf_hash *= p
            suf_hash += h(s[j])
            j-=1
            
            # print(pre_hash, suf_hash)
            pre_hash %= mod
            suf_hash %= mod
            if suf_hash == pre_hash:
                ans = i+1
                
        if ans == -1:
            return ''
        return s[:ans]