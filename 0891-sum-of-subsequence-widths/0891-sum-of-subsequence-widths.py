class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
            
        return sum(pow(2, i, MOD) * num - pow(2, len(nums) - i - 1, MOD) * num for i, num in enumerate(sorted(nums))) % MOD