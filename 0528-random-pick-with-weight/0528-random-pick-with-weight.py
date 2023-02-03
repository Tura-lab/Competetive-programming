class Solution:

    def __init__(self, w: List[int]):
        self.indices = [i for i in range(len(w))]
        tot = sum(w)
        self.total = tot
        self.probs = [w[i] / tot for i in range(len(w))]

    def pickIndex(self) -> int:
        return random.choices(self.indices, self.probs)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()