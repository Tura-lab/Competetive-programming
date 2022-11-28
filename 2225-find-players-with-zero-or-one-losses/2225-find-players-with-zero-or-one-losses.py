class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:

        counts = Counter()
        
        for a,b in matches:
            counts[a] = max(counts[a], 0)
            counts[b] += 1
        
        ans = [[], []]
        
        for name, count in sorted(list(counts.items())):
            
            if count == 0:
                ans[0].append(name)
            elif count == 1:
                ans[1].append(name)
                
        return ans