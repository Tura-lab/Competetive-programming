class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        count = 0
        for i in range(k):
            count += s[i] in vowels
        
        ans = count
        i = 0
        for j in range(k, len(s)):
            count += s[j] in vowels
            count -= s[i] in vowels
            i += 1            

            ans = max(ans, count)
            
        return ans