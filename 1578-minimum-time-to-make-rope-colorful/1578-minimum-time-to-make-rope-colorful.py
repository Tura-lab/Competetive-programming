class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tot = cur = neededTime[0]
        count = 1
        ans = 0
        for i in range(1, len(colors)):
            if colors[i] == colors[i-1]:
                tot += neededTime[i]
                cur = max(cur, neededTime[i])
            else:
                ans += tot-cur
                tot = neededTime[i]
                cur = neededTime[i]
        ans += tot-cur
        return ans