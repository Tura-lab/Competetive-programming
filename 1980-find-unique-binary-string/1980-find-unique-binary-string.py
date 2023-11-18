class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums[0])
        nums = set([int(num, 2) for num in nums])
        
        for num in range(2 ** l):
            if num not in nums:
                ans = str(bin(num))[2:]
                
                return "0" * (l - len(ans)) + ans