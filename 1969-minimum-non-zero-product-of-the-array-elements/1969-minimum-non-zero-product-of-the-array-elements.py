class Solution:
    '''
     1    6    1    6    1    6    7
    001, 110, 001, 110, 001, 110, 111
    '''
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9 + 7
        return (pow(2**p -2, 2**(p-1)-1, mod) * (2**p-1)) % mod