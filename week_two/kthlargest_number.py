class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = sorted([int(n) for n in nums])
        return str(nums[-k])
