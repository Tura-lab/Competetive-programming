class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(speed)
        time_rem = [dist[i] / speed[i] for i in range(n)]
        
        time_rem.sort()
        
        time = 0
        i = 0
        while i < n:
            if time >= time_rem[i]:
                break
            
            i += 1
            time += 1
            
        return i