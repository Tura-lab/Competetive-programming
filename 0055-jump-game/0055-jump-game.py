class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        furthest = 0
        
        for i in range(n-1):
            furthest = max(furthest, min(n-1, i + nums[i]))
            if furthest == i:
                return False
        
        
        return True