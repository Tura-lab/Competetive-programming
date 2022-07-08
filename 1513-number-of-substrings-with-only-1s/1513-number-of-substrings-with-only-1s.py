class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        start = None
        mod = 10**9 + 7
        
        for i in range(len(s)):
            if s[i] == '1':
                if start==None: 
                    start = i
                    
                ans += i-start+1
            else:
                start = None
                
        return ans%mod
                
        