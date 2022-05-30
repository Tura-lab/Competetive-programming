class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        dp = {}
        def dfs(i):
            if i>=len(nums):
                return 0
            cur = nums[i]
            j=i+1
            if i not in dp:
                tot = nums[i]
                cur = nums[i]
                
                i+=1
                j=i
                
                
                while i<len(nums) and nums[i]==cur:
                    tot+=cur
                    i+=1

                while i<len(nums) and nums[i] == cur+1:
                    i+=1
                    
                dp[j-1] = max(tot + dfs(i), dfs(j))
                
            return dp[j-1]
        
        return dfs(0)