class Solution:
    '''
     [1,3,2]         [2,4,3]         [4,5,2]
    '''
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda event:event[1])
        
        def binSearch(start, end, val):
            ans=-1
            while end>=start:
                mid = (start+end)//2
                if val > events[mid][1]:
                    start = mid+1
                    ans=mid
                else:
                    end = mid-1
            return ans
        
        best=0
        arr = []
        for i in range(len(events)):
            best = max(best, events[i][-1])
            arr.append(best)
        
        ans = 0
        for i in range(len(events)):
            idx = binSearch(0,i-1, events[i][0])
            
            if idx==-1:
                ans = max(ans, events[i][-1])
            else:
                ans = max(ans, events[i][-1]+arr[idx])
        
        return ans