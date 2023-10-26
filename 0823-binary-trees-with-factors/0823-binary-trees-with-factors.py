class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        arr_set = set(arr)
        MOD = 10 ** 9 + 7
                                
        dp = defaultdict()
        for num in arr:
            dp[num] = 1
            
        for num in arr:
            for num2 in arr:
                if num / num2 in arr_set:
                    dp[num] += dp[num2] * dp[num / num2]
                    dp[num] %= MOD
        
        return sum(dp.values()) % MOD