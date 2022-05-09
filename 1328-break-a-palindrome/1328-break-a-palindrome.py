class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        
        ans = list(palindrome)
        for i in range(len(palindrome)):
            if palindrome[i]!='a' and i!=len(palindrome)//2:
                ans[i]='a'
                return ''.join(ans)
            
        ans[-1]='b'
        return ''.join(ans)