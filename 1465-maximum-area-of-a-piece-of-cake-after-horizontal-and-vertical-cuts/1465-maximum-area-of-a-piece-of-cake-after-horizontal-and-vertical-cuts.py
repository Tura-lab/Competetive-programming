class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.append(0)
        verticalCuts.append(0)
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        horizontalCuts.sort()
        verticalCuts.sort()
        
        mod = 10**9 + 7
        max_hor = max_ver = 0
        
        for i in range(1, len(horizontalCuts)):
            max_hor = max(max_hor, horizontalCuts[i] - horizontalCuts[i-1])
        for i in range(1, len(verticalCuts)):
            max_ver = max(max_ver, verticalCuts[i] - verticalCuts[i-1])
        
        return (max_hor%mod * max_ver%mod)%mod