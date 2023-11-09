from sortedcontainers import SortedList

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        sl = []
        old_nums = nums.copy()
        
        for i in range(len(nums)):
            nums[i] -= i

        for i, num in enumerate(nums):
            if old_nums[i] > 0:

                idx = bisect_right(sl, (num, float('inf')))
                if idx:
                    _, old_sum = sl[idx - 1]
                    new_sum = old_sum + old_nums[i]
                    sl.insert(idx, (num, max(old_nums[i], new_sum)))

                else:
                    sl.insert(0, (num, old_nums[i]))
                    new_sum = old_nums[i]

                while idx + 1 < len(sl) and sl[idx + 1][1] < sl[idx][1]:
                    sl.remove(sl[idx + 1])

        return max(b for a, b in sl) if sl else max(old_nums)