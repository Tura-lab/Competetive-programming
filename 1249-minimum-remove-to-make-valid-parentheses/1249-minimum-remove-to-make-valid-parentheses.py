class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        lee(t(c)o)de)
        ( ( ) ) ) 
        
        ( ( ) ) 
        ( ( ) 
        """
        
        closing = dict()
        ans = []
        stack = []
        for i, char in enumerate(s):
            if char not in '()':
                ans.append((i, char))
            
            else:
                if char == '(':
                    stack.append(i)
                    ans.append((i, '('))
                else:
                    if stack:
                        ans.append((i, ')'))
                        stack.pop()
                        
        new_ans, j = [], 0
        for i, char in ans:
            if j < len(stack) and stack[j] == i:
                j += 1
                continue
            new_ans.append(char)
            
        return "".join(new_ans)