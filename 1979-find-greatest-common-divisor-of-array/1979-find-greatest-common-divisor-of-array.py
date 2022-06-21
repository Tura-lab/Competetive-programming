class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = float('inf')
        mx = -float('inf')
        for num in nums:
            mn = min(mn, num)
            mx = max(mx, num)
        
        for i in range(mn, 0, -1):
            if mx%i == 0 and mn%i==0:
                return i