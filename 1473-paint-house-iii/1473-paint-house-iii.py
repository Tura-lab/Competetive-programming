class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        if 0 not in houses:
            count = 1
            for i in range(1, m):
                if houses[i]!=houses[i-1]:
                    count+=1
            return 0 if count==target else -1 
        
        editable = [0]*m
        count = 0
        for i in range(m-1, -1, -1):
            if houses[i] == 0:
                count +=1
            editable[i] = count
        
        @cache
        def solve(i, j, k):
            if i==m:
                return 0 if k==target else float('inf')
            
            if houses[i] != 0: return solve(i+1, houses[i], k if houses[i]==j else k+1)
            
            ans = float('inf')
            if k == target:
                ans = min(ans, cost[i][j-1] + solve(i+1, j, k))
            else:
                for color in range(1, n+1):
                    ans = min(ans, cost[i][color-1] + solve(i+1, color, k if color==j else k+1))
                    
            return ans
            
        
        ans = solve(0, -1, 0)
        return -1 if ans == float('inf') else ans
