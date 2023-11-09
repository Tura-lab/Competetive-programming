from sortedcontainers import SortedList

class Solution:
    def maxBalancedSubsequenceSum(self, nums: List[int]) -> int:
        sl = SortedList()
        old_nums = nums.copy()
        
        for i in range(len(nums)):
            nums[i] -= i
            
        # print(nums)
        # print(old_nums)
            
        ans = 0
        for i, num in enumerate(nums):
            if old_nums[i] > 0:

                idx = sl.bisect_right((num, float('inf')))
                # print(idx, sl, num,748374, len(sl))
                if idx:
                    _, old_sum = sl[idx - 1]
                    new_sum = old_sum + old_nums[i]
                    sl.add((num, max(old_nums[i], new_sum)))

                else:
                    sl.add((num, old_nums[i]))
                    new_sum = old_nums[i]

                # print(num, sl)
                while idx + 1 < len(sl) and sl[idx + 1][1] < sl[idx][1]:
                    sl.remove(sl[idx + 1])

        # print(list(sl))
        
        return max(b for a, b in sl) if sl else max(old_nums)