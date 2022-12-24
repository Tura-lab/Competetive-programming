class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        cur = -1
        while n:
            if cur == n%2:
                return False
            cur = n%2
            n //= 2
            
        return True