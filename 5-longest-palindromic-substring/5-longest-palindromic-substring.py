'''
b a b a d
1 1 
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(i,j):
            while -1<i-1<len(s) and -1<j+1<len(s) and s[i-1] == s[j+1]:
                i-=1
                j+=1
            return (i,j)
        ans = (0,0)
        for i in range(len(s)):
            k, l = pal(i,i)
            if l-k > ans[1]-ans[0]:
                ans = (k,l)
                
            if -1<i+1<len(s) and s[i]==s[i+1]:
                k,l = pal(i,i+1)
                if l-k > ans[1] - ans[0]:
                    ans = (k,l)
            
        return s[ans[0]: ans[1]+1]