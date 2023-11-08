class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if (sx, sy) == (fx, fy):
            return t != 1
        tot = max(abs(sx - fx), abs(sy - fy))
        
        if tot > t:
            return False
        
        return True