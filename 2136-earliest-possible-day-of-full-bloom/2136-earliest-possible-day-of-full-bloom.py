class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        plants = list(zip(plantTime, growTime))
        plants.sort(key = lambda x: x[1], reverse = True)
            
        total = 0
        curGrowing = 0
        
        last = 0
        
        for p, g in plants:

            total += p
            last = max(last, total + g)
            
        return last