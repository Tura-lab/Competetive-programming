class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(int(num**(1/2)) +1):
            if i*i == num:
                return True
        return False