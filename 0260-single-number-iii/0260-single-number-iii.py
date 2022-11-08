class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num

        count = 0
        while x & 1 == 0:
            x >>= 1
            count += 1
        
        wanted = 1 << count
        a, b = 0, 0
        
        for num in nums:
            if num & wanted:
                a ^= num
            else:
                b ^= num
        
        return [a,b]