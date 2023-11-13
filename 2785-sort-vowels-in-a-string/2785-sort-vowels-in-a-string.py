class Solution:
    def sortVowels(self, s: str) -> str:
        def isVowel(l):
            return l in 'AEIOUaeiou'
        
        s = list(s)
        v = sorted([l for l in s if isVowel(l)], key = lambda x: ord(x))
        
        i = 0
        for j in range(len(s)):
            if isVowel(s[j]):
                s[j] = v[i]
                i += 1
                
        return "".join(s)