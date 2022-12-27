class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        bags = sorted([capacity[i] - rocks[i] for i in range(len(rocks))])        
        
        count = i = 0
        while i<len(rocks) and additionalRocks - bags[i] >= 0:
            count += 1
            additionalRocks -= bags[i]
            i += 1
            
        return count