class Solution:
    def reverse(self, x: int) -> int:
        if x<0:
            ans='-'
        else:
            ans=''
        x=str(x)
        top = (2**31) - 1
        bottom = -(2**31)
        
        for i in range(len(x)-1, -1, -1):
            if x[i]!='-':
                ans+=x[i]    
        ans = int(ans)
        return ans if bottom <= ans <= top else 0