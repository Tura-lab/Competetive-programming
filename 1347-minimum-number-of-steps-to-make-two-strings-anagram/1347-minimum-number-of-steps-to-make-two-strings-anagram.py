class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        abb => 1a + 2b
        baa => 2a + 1b
        '''
        
        s = Counter(s)
        t = Counter(t)
        
        return sum(max(0, s[l] - t[l]) for l in 'abcdefghijklmnopqrstuvwxyz')