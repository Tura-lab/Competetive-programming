class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        found = set()
        ans = None
        for num in nums:
            if num in found:
                ans = num
            found.add(num)
        
        for num in range(1, len(nums)+1):
            if num not in found:
                return [ans,num]