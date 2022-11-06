class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gas = [gas[i]-cost[i] for i in range(len(gas))]
        
        # print(gas)
        start, end = 0, len(gas) - 1
        
        val = 0
        for start in range(len(gas)):
            val += gas[start]
            while val < 0 and start < end:
                val += gas[end]
                end -= 1
            
            if start == end and val < 0:
                return -1
                        
        return (end+1) % len(gas)
        