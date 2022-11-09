class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = set()
        for i in range(len(s)):
            if s[i].isalpha():
                letters.add(i)
        
        ans = []
        path = []
        def dfs(i):
            if i==len(s):
                ans.append(''.join(path))
                return
            
            if i in letters:
                #change
                path.append(s[i].upper() if s[i].islower() else s[i].lower())
                dfs(i+1)
                path.pop()

                path.append(s[i])
                dfs(i+1)
                path.pop()
            else:
                path.append(s[i])
                dfs(i+1)
                path.pop()
        
        dfs(0)
        return ans