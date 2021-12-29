class Solution:
    def calculate(self, s: str) -> int:
        temp = ''
        stack = [] 
        for i in range(len(s)):
            if s[i] not in '*/+-':
                temp+=s[i]
            else:
                stack.append(int(temp))
                stack.append(s[i])
                temp = ''
        if temp is not '':
            stack.append(int(temp))
        s = stack
        stack = []
        i=0
        
        while i< (len(s)):
            j=0
            if s[i] == '*':
                num = int(stack[-1])
                ans = num * int(s[i+1])
                stack.pop()
                stack.append(ans)
                i=i+1
            elif s[i] == '/':
                num = int(stack[-1])
                ans = num / int(s[i+1])
                stack.pop()
                stack.append(ans)
                i=i+1
            else:
                stack.append(s[i])
            i+=1
        total = int(stack[0])
        for i in range(1, len(stack), 2):
            if stack[i] == "+":
                total += int(stack[i+1])
            elif stack[i] == "-":
                total -= int(stack[i+1])
                
        return total
