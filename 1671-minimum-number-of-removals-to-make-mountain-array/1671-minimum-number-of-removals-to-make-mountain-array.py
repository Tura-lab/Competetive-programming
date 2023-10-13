class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        
        n = len(nums)
        LIS = [1] * n
        
        for j in range(len(nums)):
            for i in range(j):
                if nums[i] < nums[j]:
                    LIS[j] = max(LIS[j], 1 + LIS[i])
                    
        LDS = [1] * n
        
        for j in range(len(nums)-1, -1, -1):
            for i in range(len(nums) - 1, j, -1):
                if nums[j] > nums[i]:
                    LDS[j] = max(LDS[j], 1 + LDS[i])
                    
            
        ans = 0
        for i in range(1, n-1):
            if LDS[i] == 1 or LIS[i] == 1:
                continue
            ans = max(ans, LDS[i] + LIS[i] - 1)
            
        # print(LIS)
        # print(LDS)
        
        return n - ans