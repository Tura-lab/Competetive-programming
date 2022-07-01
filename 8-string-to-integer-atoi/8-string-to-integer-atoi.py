class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        ans = ''
        found = False
        for i in range(len(s)):
            if s[i] not in '1234567890':
                if (s[i] == ' ' or s[i] == '+') and not found:
                    if s[i] == '+':
                        found=True
                    continue
                if s[i] == '-' and not found:
                    found=True
                    sign = -1
                    continue
                
                break
            found=True
            ans += s[i]

        if found and ans:
            num = int(ans)*sign
            if num<0:
                return max(num, -2**31)
            else:
                return min(num ,2**31-1)
        return 0 
        