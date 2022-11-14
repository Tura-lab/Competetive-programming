class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = lcm(nums[j], cur)
                count += cur == k
                
                
        return count