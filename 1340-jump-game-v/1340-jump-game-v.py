class Solution:
    def maxJumps(self, nums: List[int], d: int) -> int:
        n = len(nums)
        
        left  = [0] * n
        right = [n-1] * n
        
        stack = []
        for i in range(n):
            while stack and stack[-1][0] <= nums[i]:
                num, idx = stack.pop()
                right[idx] = i - 1
            stack.append((nums[i], i))
            
        stack = []
        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] <= nums[i]:
                num, idx = stack.pop()
                left[idx] = i + 1
            stack.append((nums[i], i))
        
            
        dp = [0] * n
        
        def dfs(i):
            if dp[i] == 0:
                ans = 1

                for idx in range(max(i-d, left[i]), min(i+d+1, right[i]+1)):
                    if idx != i:
                        ans = max(ans, 1 + dfs(idx))
                
                dp[i] = ans
                    
            return dp[i]
        
        
        for i in range(n):
            if dp[i] == 0:
                dfs(i)
                
                
        # print(dp)
        return max(dp)