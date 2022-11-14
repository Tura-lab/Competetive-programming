class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            cur = nums[i]
            for j in range(i, len(nums)):
                cur = gcd(nums[j], cur)
                count += cur == k
                
        return count