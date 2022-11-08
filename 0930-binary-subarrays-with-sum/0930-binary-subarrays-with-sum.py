class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        found = defaultdict(int)
        found[0] += 1
        cur = 0
        count = 0
        for num in nums:
            cur += num
            count += found[cur-goal]
            found[cur] += 1
        
        return count