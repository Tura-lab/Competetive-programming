class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        found = {}
        pals = 0
        singles = 0
        for word in words:
            if word[::-1] in found:
                pals += 1
                found[word[::-1]]-=1
                if found[word[::-1]] == 0:
                    del found[word[::-1]]
            else:
                if word in found:
                    found[word] +=1
                else: 
                    found[word] = 1
        
        for word,count in found.items():
            if word[0] == word[1]:
                singles = 1
                break
        
        return pals*4 + singles*2