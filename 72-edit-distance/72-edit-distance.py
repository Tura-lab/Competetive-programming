class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def recurse(i, j):
            if j>=len(word2):
                return len(word1)-i
            if i>=len(word1):
                return len(word2)-j
            
            ans = float('inf')
            
            if word1[i] == word2[j]:
                # do nothing or delete
                return recurse(i+1, j+1)
            
            # insert
            ans = min(ans, 1+recurse(i, j+1))
            
            # delete
            ans = min(ans, 1+recurse(i+1, j))
            
            # replace
            ans = min(ans, 1+recurse(i+1, j+1))
            
            return ans
        
        return recurse(0,0)