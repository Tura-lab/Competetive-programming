class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def solve(n):
            if n == 1: return True
            if n in seen:return False
            
            seen.add(n)

            new = 0
            for i in str(n):
                new += int(i)**2

            return solve(new)
        
        return solve(n)