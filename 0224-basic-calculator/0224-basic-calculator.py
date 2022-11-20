class Solution:
    def calculate(self, s: str) -> int:
        new = []
        cur = ''
        for l in s:
            if l == ' ':
                continue
            
            if l in '()+-':
                if cur:new.append(cur)
                new.append(l)
                cur = ''
            else:
                cur += l
        
        if cur:new.append(cur)
                        
        s = new
        
        i = 0
        def dfs(i):                
            cur = 0
            op = 1
            while i < len(s):
                if s[i] == '(':
                    amount, idx = dfs(i+1)
                    cur += amount if op else -amount
                    i = idx-1
                elif s[i] == ')':
                    return cur, i+1
                elif s[i] == '-' or s[i] == '+':
                    op = 1 if s[i] == '+' else 0
                else:
                    cur += int(s[i]) if op else -int(s[i])
                    
                i+=1
            
            return cur
         
        return dfs(0)