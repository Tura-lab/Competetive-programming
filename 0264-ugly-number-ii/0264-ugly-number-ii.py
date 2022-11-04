class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = []
        for a in range(31):
            for b in range(20):
                for c in range(14):
                    nums.append(2**a * 3**b * 5**c)
    
        nums.sort()
        return nums[n-1]