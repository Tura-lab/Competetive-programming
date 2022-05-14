class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1) 
        '''
        0  0000 0
        1  0001 1
        2  0010 1
        3  0011 2
        
        4  0100 1
        5  0101 2
        6  0110 2
        7  0111 3
        
        8  1000 1
        9  1001 2
       10  1010 2
       11  1011 3
       12  1100 2
       13  1101
       14  1110
       15  1111
        '''
        power = 1
        num = 1
        for i in range(1,n+1):
            if i == num<<1:
                num <<= 1
            ans[i] = ans[i-num] +1
        
        return ans
        