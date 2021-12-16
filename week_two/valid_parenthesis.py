class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if len(stack)==0:
                stack.append(i)
                continue
            if i==')' and stack[-1]=='(':
                stack = stack[:-1]
            elif i==']' and stack[-1]=='[':
                stack = stack[:-1]
            elif i=='}' and stack[-1]=='{':
                stack = stack[:-1]
            else:
                stack.append(i)
        return len(stack)==0
