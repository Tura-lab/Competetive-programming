class Solution:
    def knightDialer(self, n: int) -> int:
        mod = 10**9 +7
        m = {0:[4,6], 1:[6,8], 2:[7,9], 3:[4,8], 4:[0,3,9], 5:[], 6:[1,7,0], 7:[2,6], 8:[1,3], 9:[4,2], }
        
        jumps = [[2,1],[-2,-1],[1,2],[-1,-2],[-2,1],[2,-1],[-1,2],[1,-2]]

        
        @cache
        def dfs(cur,count):
            if count == n:
                return 1
            
            ans = 0
            for v in m[cur]:
                ans = (ans + dfs(v, count+1))%mod
                
            return ans
        
        ans = 0
        for cur in range(10):
            ans = (ans + dfs(cur,1))%mod
        
        return ans