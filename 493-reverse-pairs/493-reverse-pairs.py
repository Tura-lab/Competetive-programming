from sortedcontainers import SortedList

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sorted_ = SortedList()
        count = 0
        
        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            cur = (num//2)-1 if num%2==0 else num//2
            count += sorted_.bisect_left(cur) + sorted_.count(cur)
            # print(num, sorted_, cur, count, sorted_.bisect_left(cur))
            sorted_.add(num)
            
        
        return count