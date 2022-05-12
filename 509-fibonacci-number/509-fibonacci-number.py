class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        ans = 1
        
        for i in range(2, n+1):
            ans = first + second
            first = second
            second = ans
            
        return 0 if n==0 else ans