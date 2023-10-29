class Solution:
    def checkValidString(self, s: str) -> bool:
        s = list(s)
        stars = deque()
        stack = []
        
        for i, l in enumerate(s):
            if l == '*':
                stars .append(i)
            elif l == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif stars:
                    idx = stars.popleft()
                    s[idx] = " "
                else:
                    return False

        if not stack:
            return True
        
        i, j = len(stack) - 1, len(s) - 1
        
        while i >= 0 and j >= 0:
            while j > stack[i] and s[j] != '*':
                j -= 1
                
            if j == stack[i]:
                return False
                
            i -= 1
            j -= 1
        
        return True