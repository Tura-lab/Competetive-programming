class Solution:
    '''
    [1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]
    
    [1, 6, 1]  [3, 10, 2]  [10, 12, 3]  [11, 12, 2]  [12, 15, 2]  [13, 18, 1]

    '''
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key = lambda x: x[0])
        print(len(rides))
        dp = [-1]*len(rides)

        def binSearch(start, end, val):
            ans = -1
            while start <= end:
                mid = (start+end)//2
                nxt = rides[mid][0]
                if val <= nxt:
                    ans = mid
                    end = mid-1
                else:
                    start = mid+1
            return ans
        
        def explore(i):
            if i >= len(rides) or i==-1:
                return 0
            if dp[i]!=-1:
                return dp[i]
            choose = rides[i][1]-rides[i][0]+rides[i][2] + explore(binSearch(i+1, len(rides)-1, rides[i][1]))
            dont   = explore(i+1)
            
            dp[i] = max(choose, dont)
            return dp[i]
        
        return explore(0)