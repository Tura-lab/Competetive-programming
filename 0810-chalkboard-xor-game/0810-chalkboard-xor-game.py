class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        x = 0
        
        for num in nums:
            x ^= num
            
        if x == 0:return True
        
        return len(nums)%2 == 0