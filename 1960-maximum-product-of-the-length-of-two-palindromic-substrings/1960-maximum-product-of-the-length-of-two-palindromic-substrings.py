class Solution:
    def maxProduct(self, s: str) -> int:
        
        # run manachers algo
        n = len(s)
        dp = [1] * n
        
        l, r, = 0, 0
        
        for i in range(n):
            k = 1 if i >= r else min(r - i + 1, dp[l + r - i] // 2)
            
            while i - k >= 0 and i + k < len(s) and s[i - k] == s[i + k]:
                k += 1
                
            dp[i] = 2 * k - 1
            
            if i + k - 1 > r:
                l = i - k + 1
                r = i + k - 1
                
        # print(dp)
            
        max_before = [0] * n
        max_after = [0] * n
        
        for i in range(n):
            start, end = i - dp[i]//2, i + dp[i]//2
            max_before[end] = max(max_before[end], dp[i])
            
        for i in range(n-2, -1, -1):
            max_before[i] = max(max_before[i], max_before[i+1] - 2)
            
        for i in range(n):
            start, end = i - dp[i]//2, i + dp[i]//2
            max_after[start] = max(max_after[start], dp[i])
            
        for i in range(1, n):
            max_after[i] = max(max_after[i], max_after[i - 1] - 2)
            
        max_before = list(accumulate(max_before, max))
        max_after = list(accumulate(max_after[::-1], max))[::-1]
            
        ans = 0
        for i in range(n-1):
            ans = max(ans, max_before[i] * max_after[i + 1])

        return ans