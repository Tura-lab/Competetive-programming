class Solution:
    def tribonacci(self, n: int) -> int:
        first = 0
        if n ==0:
            return first
        second = 1
        if n == 1:
            return second
        third = 1
        fourth = 2
        if n == 2:
            return third
        
        for i in range(3, n+1):
            fourth = first + second + third
            first = second
            second = third
            third = fourth
            
        return fourth