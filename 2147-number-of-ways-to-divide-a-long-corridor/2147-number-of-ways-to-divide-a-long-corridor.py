class Solution:
    def numberOfWays(self, corridor: str) -> int:
        if corridor.count('S')&1 or corridor.count('S')==0:
            return 0
        
        mod = 10**9+7
        counts = 1
        last = None
        found = 0
        for i in range(len(corridor)):
            if corridor[i] == 'S' and found>1 and found&1 == 0:
                counts *= (i-last)
                counts%=mod
            
            if corridor[i] == 'S':
                last = i
                found +=1
                
        return counts
                
                