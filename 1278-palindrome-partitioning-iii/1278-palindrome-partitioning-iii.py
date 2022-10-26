class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        pals = [[float('inf')] * len(s) for _ in range(len(s))]
        def check(i, j):
            left, right = i, j
            count = 0
            while i>=0 and j<len(s):
                if s[i] != s[j]:
                    count += 1
                pals[i][j] = count
                i-=1
                j+=1
                
        for i in range(len(s)):
            check(i, i)
            if i < len(s)-1:
                check(i, i+1)
                
        @cache
        def dfs(i, j, rem):
            if j == len(s):
                if rem == 0 and i == j:
                    return 0
                return float('inf')
            
            return min(dfs(i, j+1, rem), pals[i][j] + dfs(j+1, j+1, rem - 1))
        
        return dfs(0, 0, k)