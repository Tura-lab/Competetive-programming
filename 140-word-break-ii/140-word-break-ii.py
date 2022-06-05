class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        d = set(wordDict)
        final = []
        
        @cache
        def solve(j, found):
            if j>=len(s):
                return final.append(found.strip())
            
            ans = False
            for i in range(j+1,len(s)+1):
                if s[j:i] in d:
                    ans = ans or solve(i, found + ' ' + s[j:i])
                    
            return ans
        
        solve(0, '')
        
        return final