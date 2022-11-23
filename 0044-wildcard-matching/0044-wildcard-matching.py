class Solution:
    def isMatch(self, s: str, p: str) -> bool:
#         newp = []
#         for l in p:
#             if not newp:
#                 newp.append(l)
#                 continue
#             if l == '*' and p[-1] == '*':continue
#             newp.append(l)
        
#         p = ''.join(newp)
        # print(p)
        @cache
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            # if i == len(s):
            #     return j == len(p) or (j == len(p)-1 and p[j] == '*')
            
            if p[j] == '*':
                while j+1 < len(p) and p[j+1] == '*':
                    j+=1
                while i <= len(s):
                    if dfs(i, j+1):
                        return True
                    i += 1
                return False
            
            elif i == len(s):
                return j == len(p)
            
            elif p[j] == '?':
                return dfs(i+1, j+1)
            
            elif p[j] != s[i]:
                return False
            
            return dfs(i+1, j+1)
        
        return dfs(0, 0)