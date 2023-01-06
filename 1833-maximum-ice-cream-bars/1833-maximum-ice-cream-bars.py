class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        return sum(1 for num in sorted(costs) if (coins := coins-num) >= 0)