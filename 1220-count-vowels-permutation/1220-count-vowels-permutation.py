class Solution:
    def countVowelPermutation(self, n: int) -> int:
        followers = {
            -1:[0,1,2,3,4],
            0: [1],
            1: [0,2],
            2: [0,1,3,4],
            3: [2,4],
            4: [0]
        }
        mod = 10**9 +7
        
        @cache
        def dfs(length, last):
            if length==n:
                return 1
            
            ans = 0
            for v in followers[last]:
                ans = (ans + dfs(length+1, v))%mod
                
            return ans
        
        return dfs(0, -1)
        