class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        new = [points[0]]
        
        for i in range(1, len(points)):
            point = points[i]
            if point[0] <= new[-1][1]:
                new[-1] = [max(point[0], new[-1][0]),min(point[1], new[-1][1])]
            else:
                new.append(point)
        
        # print(points,89898)
        # print(new)
        
        return len(new)