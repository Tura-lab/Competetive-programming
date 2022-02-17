from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        return ''.join([i*j for i,j in sorted([ (i,j) for i,j in d.items() ], reverse=True, key = lambda item: item[1])])
        
        