class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
                
        @cache
        def dfs(n, k):
            if k == 0:
                return float('inf')
            if k == 1:
                return n
            if n == 1 or n == 0:
                return n
            
            ans = float('inf')
            row = []
            l, r = 1, n - 1
            
            while l <= r:
                j = l + (r - l) // 2
                
                breaks = dfs(n - j, k - 1)
                survives = dfs(j - 1, k)
                
                ans = min(ans, 1 + max(breaks, survives))
                
                if breaks > survives:
                    l = j + 1
                else:
                    r = j - 1
                
            
            
            return ans
    
        return dfs(n, k)