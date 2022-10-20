from random import randint
from sortedcontainers import SortedList

class RandomizedSet:

    def __init__(self):
        self.nums = SortedList()
        

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.nums.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        idx = randint(0, len(self.nums)-1)
        return self.nums[idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()