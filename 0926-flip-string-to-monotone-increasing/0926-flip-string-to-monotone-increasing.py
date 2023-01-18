class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        '''
        00110
        0011
        '''
        zeros = s.count('0')
        ones = 0
        
        ans = zeros
        
        for i in range(len(s)):
            ones  += s[i] == '1'
            zeros -= s[i] == '0'
            
            ans = min(ans, ones + zeros)
        
        return ans