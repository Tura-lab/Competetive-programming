class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:

        mod = 10 ** 9 + 7
        n = len(nums)
        
        counts = [0] * 31
        nums.sort(reverse=True)
        
        for num in nums:
            for i in range(31):
                if 1 << i & num:
                    counts[i] += 1
                    
        for j in range(len(nums)):
            for i in range(31):
                if counts[i]:
                    nums[j] = nums[j] | 1 << i
                    counts[i] -= 1
                else:
                    nums[j] = nums[j] & (~(1 << i))
                    
        nums.sort(reverse=True)
        tot = 0
        for i in range(k):
            tot += nums[i] ** 2
            tot %= mod
            
        return tot