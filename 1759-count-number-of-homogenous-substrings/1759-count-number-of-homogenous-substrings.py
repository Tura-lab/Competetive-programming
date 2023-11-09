class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        
        ans = 0
        count, past = 0, None
        for i, l in enumerate(s):
            if l == past:
                count += 1
            else:
                past = l
                count = 1
            
            ans += count
            ans %= MOD
                
        return ans