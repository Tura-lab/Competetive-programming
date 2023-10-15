class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = 10 ** 9 + 7
        tot = steps
        @cache
        def dfs(steps, cur):
            if not 0 <= cur <= arrLen-1:
                return 0
            if steps == 0:
                return cur == 0
            
            return (dfs(steps - 1, cur - 1) + dfs(steps - 1, cur + 1) + dfs(steps - 1, cur )) % mod
        
        return dfs(steps, 0)