from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        d = list(Counter(s).items())
                
        heap = []
        for i in range(len(d)):
            letter, count = d[i]
            heapq.heappush(heap, (-count, i, letter*count))
            
        return ''.join([heapq.heappop(heap)[-1] for i in range(len(heap))])