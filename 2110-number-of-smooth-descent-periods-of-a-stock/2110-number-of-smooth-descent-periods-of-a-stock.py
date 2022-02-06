class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = len(prices)
        val = 0
        for i in range(1, len(prices)):
            if prices[val] == prices[i]+(i-val):
                ans+=(i-val)
            else:
                val=i
        return ans