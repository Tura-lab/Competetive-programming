class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        ans = []
        def solve(cur,pos):
            if len(cur) == len(digits):
                return ans.append(cur)
            
            for i in range(pos,pos+1):
                for j in range(len(d[digits[i]])):
                    letter = d[digits[i]][j]
                    solve(cur + letter, pos+1)
                                  
        solve('',0)
        return ans