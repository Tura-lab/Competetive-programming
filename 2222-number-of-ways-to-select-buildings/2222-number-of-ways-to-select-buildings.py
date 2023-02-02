class Solution:
    def numberOfWays(self, s: str) -> int:
        
        zero_1 = 0
        zero_2 = 0
        zero_3 = 0
        
        one_1 = 0
        one_2 = 0
        one_3 = 0
        
        for l in s:
            if l == '0':
                zero_1 += 1
                zero_2 += one_1
                zero_3 += one_2
            else:
                one_1 += 1
                one_2 += zero_1
                one_3 += zero_2
                
                
        return zero_3 + one_3