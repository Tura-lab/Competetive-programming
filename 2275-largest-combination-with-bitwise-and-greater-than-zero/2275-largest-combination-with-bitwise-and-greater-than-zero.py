class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        
        for i in range(31, -1, -1):
            for num in nums:
                if (1<<i)&num != 0:
                    counts[i] += 1
        
        return max(counts.values())