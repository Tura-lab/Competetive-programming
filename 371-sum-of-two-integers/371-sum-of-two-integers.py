class Solution:
    def getSum(self, a: int, b: int) -> int:
        i=0
        while i<=32:
            carry = a&b 
            a ^= b 
            b = carry<<1
            i+=1
        return a &(2**32-1) if b>(2**32-1) else a