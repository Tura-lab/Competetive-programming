class Solution:
    '''
    time = 1   2   3 , num = 5
    
    low = 1
    high = 5*1 = 5
    mid = (1+5)//2 = 3
    '''
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # print(len(time))
        time.sort()
        low = time[0]
        high = low*totalTrips
        ans = high
        
        while low<=high:
            mid = (low+high)//2
            tot = 0
            
            for t in time:
                tot += mid//t
                
            if tot < totalTrips:
                low=mid+1
            else:
                ans = min(ans, mid)
                high = mid-1
        return ans
                