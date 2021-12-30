class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        citations.sort()
        for i in range(n-1, -1, -1):
            if citations[i] < (n-i)-1:
                return (n-i)-1
            if (n-i) >= citations[i]:
                return citations[i]
        return n
