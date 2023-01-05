class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        
        new = []
        
        for x, y in points:
                
            if new and new[-1][1] >= x:
                new[-1] = [ max(new[-1][0], x), min(new[-1][1], y) ]
            
            else:
                new.append([x, y])
                
        return len(new)