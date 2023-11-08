class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty: # reversing the operations
            tx, ty = tx % ty, ty % tx
            
        if sx == ty and sy == ty: # succesfully reversed
            return True
        elif sx == tx and sy < ty: # ty went too low
            return abs(sy - ty) % sx == 0 #  we can use sx to bring up sy to ty
        elif sy == ty and sx < tx: # tx went too low
            return abs(sx - tx) % sy == 0
        
        return False