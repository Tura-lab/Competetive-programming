class Solution:
    def reverseParentheses(self, s: str) -> str:
        closing = opening = 0
        i=0
        while i<len(s):
            if s[i] == ')':
                closing = i
                j=i-1
                while s[j] != '(':
                    j-=1
                opening=j
                s = s[:opening+1] + s[opening+1:closing][::-1] + s[closing:]
                s = s[:opening] + ' ' + s[opening+1:closing] + ' ' + s[closing+1:]
            i+=1
        return s.replace(' ', '')
