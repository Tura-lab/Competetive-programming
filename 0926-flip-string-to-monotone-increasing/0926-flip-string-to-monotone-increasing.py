class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        00110
        00
        '''
        
        @cache
        def dfs(i, turn):
            if i == len(s):
                return 0
            
            ans = float('inf')
            if turn == 0:
                ans = min(ans, (s[i] == '1') + min(dfs(i+1, turn), dfs(i+1, 1-turn)))
                
            if turn == 1:
                ans = min(ans, (s[i] == '0') + dfs(i+1, turn))
                
            return ans
        
        return min(dfs(0, 0), dfs(0, 1))
            