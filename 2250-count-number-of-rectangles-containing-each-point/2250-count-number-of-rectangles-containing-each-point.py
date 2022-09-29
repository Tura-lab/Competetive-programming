class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        heights = [[] for _ in range(101)]
        rectangles.sort(key = lambda x: x[0])
        '''
        r 
        p
        
        plogr
        '''
        
        for x, y in rectangles:
            heights[y].append(x)
            
        ans = [0]*len(points)
        
        for j in range(len(points)):
            x,y = points[j]
            for i in range(len(heights)):
                if i < y:continue
                
                l = 0
                r = len(heights[i])-1
                valid = r+1
                while l<=r:
                    mid = l + (r-l)//2
                    if heights[i][mid] >= x:
                        valid = mid
                        r = mid-1
                    else:
                        l = mid+1
                
                ans[j] += len(heights[i]) - valid
                
        return ans