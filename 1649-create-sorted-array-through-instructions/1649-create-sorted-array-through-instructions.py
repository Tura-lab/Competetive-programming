from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        ll = SortedList()
        tot = 0
        mod = 10**9+7
        
        for num in instructions:
            tot = tot + min(ll.bisect_left(num), len(ll)-ll.bisect_right(num))
            ll.add(num)
            
        return tot % mod
        