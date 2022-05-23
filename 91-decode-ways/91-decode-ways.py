class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        for i in range(len(s)-1):
            if int(s[i])>2 and int(s[i+1])== 0:
                return 0
            if s[i] == s[i+1] == '0':
                return 0
        
        @cache
        def dfs(i):
            if i>=len(s):
                return 1
            if s[i] == '0':
                return 0
            tot = 0
            
            tot += dfs(i+1)
            if int(s[i])<3 and i<len(s)-1 and (i+1<len(s) and int(s[i]+s[i+1])<27):
                tot += dfs(i+2)
            
            return tot
            
        return dfs(0)