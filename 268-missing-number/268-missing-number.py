class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = len(nums)
        for i in range(len(nums)):
            ans += (i-nums[i])
        return ans
            
        
#         ## xor
#         ans = 0
#         for i in range(len(nums)+1):
#             ans ^= i
            
#         for num in nums:
#             ans ^= num

#         return ans