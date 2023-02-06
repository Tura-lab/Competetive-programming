class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        # print(len(words))
        words.sort(key = lambda x: len(x))
        
        def valid(a, b):
            if not len(a) == len(b) -1:
                return False
            i=j=0
            while i<len(a) and j<len(b):
                while j<len(b) and a[i] != b[j]:
                    j+=1
                    if j>i+1:
                        return False
                i+=1
                j+=1
            return i == len(a)
        
        # print(valid('b', 'ba'))
        ans = 1
        dp = [1]*len(words)
        for i in range(1, len(words)):
            for j in range(i-1, -1, -1):
                if len(words[i]) > len(words[j])+1:
                    break
                if not (valid(words[j], words[i])):
                    continue

                dp[i] = max(dp[i], 1 + dp[j])
                ans = max(ans, dp[i])
        
        # print(words)
        # print(dp)
        return ans
        