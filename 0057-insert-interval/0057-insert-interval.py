class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        
        intervals.sort()
        
        '''
          x, y 
        a, b
        '''
        
        ans = []
        
        for x, y in intervals:
            if not ans: ans.append([x,y])
                
            a, b = ans[-1]
            
            if x <= b:
                ans[-1] = [min(a,x), max(b,y)]
                
            else:
                ans.append([x,y])
                
                
        return ans