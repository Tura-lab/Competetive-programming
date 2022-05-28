class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(o,s):
            if o==0 and len(s) == 2*n:
                return ans.append(s)
            if o<0 or o>n or len(s)>2*n:
                return
            
            dfs(o+1, s + '(')
            dfs(o-1, s + ')')
            
            
        dfs(0,'')
        return ans
        