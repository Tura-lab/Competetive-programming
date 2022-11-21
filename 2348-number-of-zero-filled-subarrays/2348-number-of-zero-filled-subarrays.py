class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        last = None
        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if last != None:
                    count += i-last+1
                else:
                    last = i
                    count += 1
            else:
                last = None
        
        return count