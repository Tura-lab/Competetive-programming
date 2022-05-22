class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [(int(k.split(':')[0]),int(k.split(':')[1])) for k in timePoints]
        times.sort(key = lambda x: (x[0],x[1]))
                
        max_dif = 24*60
        
        _min = float('inf')
        
        cur_dif = abs( (times[-1][0]-times[0][0])*60  + times[-1][1]-times[0][1])
        _min = min(_min, max_dif-cur_dif, cur_dif)
        
        for i in range(len(times)-1):
            cur_dif = (times[i+1][0]-times[i][0])*60  + times[i+1][1]-times[i][1]
            _min = min(_min, max_dif-cur_dif, cur_dif)
            
        return _min