class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)
        
        @cache
        def solve(j):
            if j>=len(s):
                return True
            
            ans = False
            for i in range(j+1,len(s)+1):
                if s[j:i] in d:
                    ans = ans or solve(i)
                    
            return ans
        
        return solve(0)