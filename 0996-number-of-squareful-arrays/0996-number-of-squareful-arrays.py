class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def check(num):
            val = sqrt(num)
            return val == int(val)
        
        nums.sort()
        nexts = [i + 1 for i in range(len(nums))]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] == nums[i]:
                nexts[i] = nexts[i + 1]
        
        @cache
        def dfs(past, count, mask):
            if count == len(nums):
                return 1
            
            ans = 0
            i = 0
            while i < len(nums):
                if mask & 1 << i != 0: # alredy taken
                    i += 1
                    continue
                    
                if past == -1 or check(nums[i] + past):
                    ans += dfs(nums[i], count + 1, mask | 1 << i)
                    
                i = nexts[i]
                    
            return ans
        
        return dfs(-1, 0, 0)