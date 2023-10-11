class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        '''
        ans = [3, 3, 1]
        (size, end)
        cur = [(4, 6)]
        [1,4],[2,4],[3,6],[4,4]
                            ^
        
        [2,3,4,5]
               ^
        '''
        
        output = [-1] * len(queries)
        
        for i, interval in enumerate(intervals):
            intervals[i] = (interval, i)
        intervals.sort(key = lambda x: (x[0][0], x[0][1]))
            
        for i, query in enumerate(queries):
            queries[i] = (query, i)
        queries.sort()
        
        possible = []
        
        j = 0
        for query, i in queries:
            while j < len(intervals) and intervals[j][0][0] <= query:
                interval, idx = intervals[j]
                start, end = interval
                j += 1
                
                heappush(possible, (end - start + 1, end))
                
            while possible and possible[0][1] < query:
                heappop(possible)
                
            if possible:
                output[i] = possible[0][0]
        
        return output