class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = '/+-*'
        stack = []
        for i in tokens:
            if i not in operators:
                stack.append(int(i))
            else:
                if i == '+':
                    val = stack[-2]+stack[-1]
                    stack = stack[:-2]
                    stack.append(val)
                elif i == '-':
                    val = stack[-2]-stack[-1]
                    stack = stack[:-2]
                    stack.append(val)
                elif i == '/':
                    val = int(stack[-2]/stack[-1])
                    stack = stack[:-2]
                    stack.append(val)
                elif i == '*':
                    val = stack[-2]*stack[-1]
                    stack = stack[:-2]
                    stack.append(val)
        return stack[0]
