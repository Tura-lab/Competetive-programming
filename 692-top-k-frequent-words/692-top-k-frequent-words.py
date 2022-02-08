class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        counter = {}
        for word in words:
            if word in counter:
                counter[word]+=1
            else:
                counter[word]=1
        return [n[0] for n in sorted(counter.items(),reverse=True, key=lambda item: item[-1])[:k]]