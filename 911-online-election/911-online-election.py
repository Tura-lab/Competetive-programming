class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        
        z = 0
        o = 0 
        self.winners = []
        self.counts = {}
        _max = 0
        a = 0
        for p in persons:
            if p in self.counts:
                self.counts[p]+=1
            else:
                self.counts[p]=1
            
            if self.counts[p] >= _max:
                self.winners.append(p)
                _max = self.counts[p]
                a = p
            else:
                self.winners.append(a)
                


    def q(self, t: int) -> int:
        l = 0
        ans = r = len(self.times)-1
        
        while l<=r:
            mid = (l+r)//2
        
            if self.times[mid]==t:
                ans = mid
                break
            elif self.times[mid]<t:
                ans = mid
                l = mid+1
            else:
                r = mid-1
                
        return self.winners[ans]
            
            
            
            
            
            
            


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)