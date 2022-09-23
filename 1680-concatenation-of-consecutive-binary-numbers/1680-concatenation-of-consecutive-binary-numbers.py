class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        found = []
        for i in range(1, n+1):
            found.append(str(bin(i)))
            
        bits = ''.join([num[2:] for num in found])
        
        return int(bits, 2) % mod
