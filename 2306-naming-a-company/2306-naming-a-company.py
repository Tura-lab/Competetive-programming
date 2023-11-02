class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        '''
        ["coffee","donuts","time","toffee"]
        
        
        '''
        found = set([hash(idea) for idea in ideas])
        ans = 0
        dp = [[0] * 26 for _ in range(26)]
        
        for idea in ideas:
            curs = [hash(chr(i + ord('a')) + idea[1:]) for i in range(26)]
            for i in range(26):
                if curs[i] not in found:
                    ans += dp[i][ord(idea[0]) - ord('a')]
            for i in range(26):
                if curs[i] not in found:
                    dp[ord(idea[0]) - ord('a')][i] += 1

        return 2 * ans