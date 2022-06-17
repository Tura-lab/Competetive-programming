# from math import log, ceil
from collections import defaultdict

class RangeFreqQuery:

    def __init__(self, nums: List[int]):
        self.numbers = defaultdict(list)
        for i in range(len(nums)):
            self.numbers[nums[i]].append(i)
            
            

    def query(self, left: int, right: int, value: int) -> int:
        rng = self.numbers[value]
        # print(rng)
        l = 0
        r = len(rng)-1
        ans = r+1
        # Find left 
        while l<=r:
            mid = l + (r-l)//2
            if rng[mid] >=left:
                ans = mid
                r = mid-1
            else:
                l = mid+1
                
        l = 0
        r = len(rng)-1
        ans2 = -1
        # Find right
        while l<=r:
            mid = l + (r-l)//2
            if rng[mid]<=right:
                ans2 = mid
                l = mid+1
            else:
                r = mid-1
        
        return ans2-ans+1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)