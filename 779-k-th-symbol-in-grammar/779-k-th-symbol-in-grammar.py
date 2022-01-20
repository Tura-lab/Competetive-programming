class Solution:
    def __init__(self):
        self.val = {1:0, 0:1}
#     def __init__(self):
#         self.prev = None
#     def replace(self, s):
#         new = ''
#         for i in s:
#             if i=='0':
#                 new += '1'
#             else:
#                 new += '0'
#         return new
#     def ans(self, n, k):
#         if n == 1:
#             return '0'
#         ans = self.ans(n-1, k)
#         return ans + self.replace(ans)
        
    # def kthGrammar(self, n, k):
#         return self.ans(n, k)[k-1]
    def kthGrammar(self, n, k):
        if n==0:
            return 0
        if k > 2**(n-1):
            return self.val[self.kthGrammar(n-1, k-2**(n-1))]
        else:
            return self.kthGrammar(n-1, k)
'''
0  1
01  2
0110  4
01101001  8
0110100110010110  16
01101001100101101001011001101001  32
0110100110010110100101100110100110010110011010010110100110010110  64
'''