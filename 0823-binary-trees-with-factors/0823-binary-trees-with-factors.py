class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        arr_set = set(arr)
        MOD = 10 ** 9 + 7
        
        '''
        2,4,5,10
        
        '''
        
        def dfs(root):
            if root not in dp:
                ans = 1
                for num in arr:
                    if root / num in arr_set:
                        ans += dfs(num) * dfs(root / num)
                        ans %= MOD
                            
                dp[root] = ans % MOD
            return dp[root]
                                
        dp = defaultdict()
        for num in arr:
            dfs(num)
        
        return sum(dp.values()) % MOD