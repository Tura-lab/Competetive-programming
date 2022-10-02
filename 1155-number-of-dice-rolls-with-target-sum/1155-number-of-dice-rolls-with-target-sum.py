class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 +7
        
        @cache
        def dfs(dice, tot):
            if not dice and tot == target:
                return 1
            elif not dice:
                return 0
            if tot>target:
                return 0
            
            count = 0
            for num in range(k, 0, -1):
                count += dfs(dice-1, tot+num)
                
            return count%mod
        
        return dfs(n, 0)