class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points)==1: return 1
        slopes = {}
        
        for x,y in points:
            for a,b in points:
                if not(x==a and y==b):
                    den = (x-a)
                    slope = float('inf') if den==0 else (y-b)/den
                    t = (slope, x,y)
                    slopes[t] = 1
                    
        for a,b in points:
            for slope, x,y in slopes.keys():
                den = (x-a)
                if not(x==a and y==b):
                    s = float('inf') if den==0 else (y-b)/den
                    if s == slope:
                        slopes[(slope, x,y)] += 1
                    
                    
        return max(slopes.values())