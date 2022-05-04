class Solution:
    '''
    b c a d
    0 1 2 3
    
    02
    12
    22
    03
    13
    23
    
    a s d f r
    0 1 2 3 4
    
    00
    01
    02
    03
    04
    
    d f b a b c
    0 1 2 3 4 5
    
    03
    13
    23
    33
    04
    14
    24
    34
    05
    15
    25
    35
    '''
    def countVowels(self, word: str) -> int:
        ans = 0
        vowels = {'a','e','i','o','u'}
        for i in range(len(word)):
            if word[i] in vowels:
                ans += (i+1)*(len(word)-i)
                
        return ans