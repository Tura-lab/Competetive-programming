class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return list(map(int, (list(str(int(''.join([str(n) for n in num])) + k)))))