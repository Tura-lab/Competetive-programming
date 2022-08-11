class Solution:
    def largestCombination(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        
        ans = 0
        for i in range(31, -1, -1):
            for num in nums:
                if (1<<i)&num != 0:
                    counts[i] += 1
                    ans = max(ans, counts[i])
        
        return ans