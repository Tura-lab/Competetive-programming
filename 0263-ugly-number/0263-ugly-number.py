class Solution:
    def isUgly(self, n: int) -> bool:
        nums = [5,3,2]
        
        i = 0
        while i<3 and n>1:
            if n % nums[i] == 0:
                n //= nums[i]
            else:
                i += 1
        
        return n == 1