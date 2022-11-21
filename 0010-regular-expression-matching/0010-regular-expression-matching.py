class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if i == len(s) and not (j+1 < len(p) and p[j+1] == '*'):
                return j == len(p) or (j == len(p)-2 and p[j+1] == '*')
            if j == len(p):
                return i == len(s)
            
            if j+1 < len(p) and p[j+1] == '*':
                while i < len(s) and (p[j] == '.' or s[i] == p[j]):
                    if dfs(i, j+2):
                        return True
                    i += 1
                
                return dfs(i, j+2)
            
            elif p[j] == '.':
                return dfs(i+1, j+1)
            
            else:
                if p[j] != s[i]:
                    return False
                return dfs(i+1, j+1)
            
        return dfs(0, 0)