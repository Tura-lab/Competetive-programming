class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        lee(t(c)o)de)
        ( ( ) ) ) 
        
        ( ( ) ) 
        ( ( ) 
        """
        ans = []
        count = 0
        for i, char in enumerate(s):
            if char not in '()':
                ans.append(char)
            
            else:
                if char == '(':
                    count += 1
                    ans.append(char)
                else:
                    if count:
                        count -= 1
                        ans.append(char)
                        
        new_ans = []
        count = 0
        for i in range(len(ans) - 1, -1, -1):
            char = ans[i]
            if char not in '()':
                new_ans.append(char)
            
            else:
                if char == ')':
                    count += 1
                    new_ans.append(char)
                else:
                    if count:
                        new_ans.append(char)
                        count -= 1
        
        return "".join(new_ans[::-1])