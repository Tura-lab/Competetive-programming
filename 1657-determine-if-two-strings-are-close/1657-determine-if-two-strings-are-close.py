class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        bba
        aab
        '''
        return sorted(list(Counter(word1).values())) == sorted(list(Counter(word2).values())) and set(list(word1)) == set(list(word2))