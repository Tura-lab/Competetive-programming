class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        nums = sorted(nums)

        for i, num in enumerate(nums):
            ans += pow(2, i, MOD) * num - pow(2, len(nums) - i - 1, MOD) * num
            
        return ans % MOD