class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = float('inf')
        
        for num in nums:
            if abs(num) < abs(ans):
                ans = num
            if abs(num) == abs(ans):
                ans = max(ans,num)
                
        return ans