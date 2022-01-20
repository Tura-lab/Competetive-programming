class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                if s[i] in '1234567890':
                    if stack and stack[-1][-1] in '1234567890':
                        stack[-1] += s[i]
                    else:
                        stack.append(s[i])
                else:
                    stack.append(s[i])
            
            else:
                j=len(stack)-1
                while j>-1 and stack[j] != '[':
                    j-=1
                stack[j-1:] = (stack[j+1:]) * int(stack[j-1])
        return ''.join(stack)
