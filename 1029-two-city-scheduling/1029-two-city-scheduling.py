class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        '''
        -10, -170, 10, 350
        [[10,20],[30,200],[30,20],[400,50]]
        10, 30, 30, 400
        20, 200, 20, 50
        '''
        new = sorted([(costs[i][0] - costs[i][1], i) for i in range(len(costs))])
        
        ans = 0
        for i in range(n):
            ans += costs[new[i][1]][0]
            
        for i in range(n, len(costs)):
            ans += costs[new[i][1]][1]
        
        return ans