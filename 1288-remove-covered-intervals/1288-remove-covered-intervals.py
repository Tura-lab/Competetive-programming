class Solution:
    '''
     [1,4]   [2,8]   [3,6]
     [[1,4],[3,6],[2,8],[1,5],[2,6],[3,8]]
     [[1,2],[2,2],[3,4]]
    '''
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        rem = 0
        intervals.sort(key = lambda item: item[0])
        key = intervals[0]
        for i in range(1, len(intervals)):
            if key[0]==intervals[i][0] or key[1]>=intervals[i][1]:
                rem+=1
                if key[1]<=intervals[i][1]:
                    key = intervals[i]
            else:
                key = intervals[i]
        return len(intervals)-rem