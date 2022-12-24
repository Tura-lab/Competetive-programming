class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9 +7
        @cache
        def dfs(dif, i):
            if i == n:
                return 1 if not dif else 0
            if i>n:
                return 0
            
            if dif == 0:
                ans = dfs(-1, i+2) + dfs(0,i+1) + dfs(1, i+2) + dfs(0, i+2)
            if dif==1:
                ans = dfs(-1, i+1) + dfs(0, i+1)
            if dif== -1:
                ans = dfs(0,i+1) + dfs(1, i+1)

            return ans%mod
                
        return dfs(0,0)