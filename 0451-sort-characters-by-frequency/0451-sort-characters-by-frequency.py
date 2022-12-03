class Solution:
    def frequencySort(self, s: str) -> str:      
        counter = Counter(s)
        return ''.join(sorted(list(sorted(s)), key = lambda l: counter[l], reverse = True))