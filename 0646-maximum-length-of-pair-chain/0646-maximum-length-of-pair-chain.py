class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key = lambda x: (x[1], x[0]))
        dp = [1] * len(pairs)
        
        for j in range(1, len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], 1 + dp[i])
                    
        return max(dp)