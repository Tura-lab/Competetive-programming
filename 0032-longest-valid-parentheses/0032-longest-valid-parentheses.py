class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        stack = [('#', -1)]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(('(', i))
            else:
                if stack and stack[-1][0] == '(':
                    stack.pop()
                    ans = max(ans, i - stack[-1][1])
                else:
                    stack.append((')', i))
                    
        return ans