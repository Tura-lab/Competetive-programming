class Solution:
    def minCut(self, s: str) -> int:
        pals = [[0] * len(s) for _ in range( len(s))]
        
        def check(i,j):
            while i>=0 and j<len(s) and s[i] == s[j]:
                pals[i][j] = 1
                i-=1
                j+=1
                
        
        for i in range(len(s)):
            check(i, i)
            if i < len(s)-1:
                check(i, i+1)
        
        # print(pals)
        
        @cache
        def dfs(i, j):
            if j == len(s):
                if i == len(s):
                    return 0
                return float('inf')
            
            ans = dfs(i, j+1)
            if pals[i][j]:
                ans = min(ans, 1 + dfs(j+1, j+1))
            
            return ans
            
        return dfs(0, 0) - 1