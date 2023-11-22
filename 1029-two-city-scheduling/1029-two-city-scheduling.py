class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        '''
        -10, -170, 10, 350
        [[10,20],[30,200],[30,20],[400,50]]
        10, 30, 30, 400
        20, 200, 20, 50
        '''
        costs.sort(key = lambda x: x[0] - x[1])
        
        ans = 0
        for i in range(n):
            ans += costs[i][0]
            
        for i in range(n, len(costs)):
            ans += costs[i][1]
        
        return ans