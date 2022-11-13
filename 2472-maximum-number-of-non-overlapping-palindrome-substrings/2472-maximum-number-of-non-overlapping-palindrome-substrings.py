class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        '''
        Input: s = "abaccdbbd", k = 3
        '''
        # if len(set(s)) == 1:
        #     return len(s) // k
        
        pals = dict()
        def check(i,j):
            while i>-1 and j<len(s) and s[i] == s[j]:
                if j-i+1 >=k and (i not in pals or j-i < pals[i]-i):
                    pals[i] = j                    
                i-=1
                j+=1
            
        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
                
        pals = sorted([(i,j) for i,j in pals.items()], key = lambda x: x[1])
        count = 0
        past = -1
        for i in range(len(pals)):
            if pals[i][0] > past:
                past = pals[i][1]
                count += 1
                
        return count
        