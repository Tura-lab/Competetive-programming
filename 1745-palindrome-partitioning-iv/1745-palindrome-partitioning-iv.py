class Solution:
    def checkPartitioning(self, s: str) -> bool:
        pals = [[0] * len(s) for _ in range( len(s))]
        def check(i,j):
            while i>=0 and j<len(s) and s[i] == s[j]:
                pals[i][j] = 1
                i-=1
                j+=1
        
        for i in range(len(s)):
            check(i, i)
            if i < len(s)-1:
                check(i, i+1)
                
        for j in range(1, len(s) - 1):
            for i in range(1, j+1):
                if pals[0][i-1] and pals[i][j] and pals[j+1][len(s)-1]:
                    return True
        
        return False