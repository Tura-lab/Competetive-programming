class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        print(len(b))
        num = ''.join(map(str, b))
        return pow(a, int(num), 1337)