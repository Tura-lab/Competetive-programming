class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = list(accumulate(travel))
        garbages = [[0] * 3 for _ in range(len(garbage))] # MGP
        for i in range(len(garbage)):
            for l in garbage[i]:
                if l == "M":
                    garbages[i][0] += 1
                elif l == "G":
                    garbages[i][1] += 1
                else:
                    garbages[i][2] += 1
            
        ans = 0
        for truck in range(3):
            last = 0
            for i in range(len(garbages)):
                if garbages[i][truck]:
                    ans += garbages[i][truck]
                    last = i
                
            if last != 0:
                ans += travel[last - 1]
                
        return ans